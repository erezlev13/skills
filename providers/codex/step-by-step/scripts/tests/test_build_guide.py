import importlib.util
import json
from pathlib import Path
import re
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'build_guide.py'
spec = importlib.util.spec_from_file_location('build_guide', SCRIPT)
build_guide = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_guide)

class BuildGuideTests(unittest.TestCase):
    def flow(self):
        return {'id':'test','revision':'1','title':'Test','steps':[{'id':'first','title':'First','instruction':'Do the first action.'}]}

    def test_fragment_and_untrusted_text(self):
        flow = self.flow()
        flow['steps'][0]['instruction'] = '</script><img src=x onerror=alert(1)> __MACHINE__   שלום'
        rendered = build_guide.build(flow)
        self.assertNotIn('<img src=x', rendered)
        embedded = re.search(r'<script type="application/json"[^>]*>(.*?)</script>',rendered,re.S).group(1)
        self.assertEqual(json.loads(embedded)['flow'], flow)
        self.assertIn('__MACHINE__', json.loads(embedded)['flow']['steps'][0]['instruction'])
        self.assertNotIn('<html', rendered)

    def test_unsafe_links(self):
        for url in ['javascript:alert(1)','data:text/html,test','https://user:pass@example.com','https://example.com/ bad']:
            flow=self.flow(); flow['steps'][0]['links']=[{'label':'link','url':url}]
            with self.assertRaises(ValueError): build_guide.build(flow)

    def test_invalid_structure(self):
        cases=[]
        f=self.flow(); f['steps']*=2; cases.append(f)
        f=self.flow(); f['steps'][0]['showIf']={'step':'future','equals':'yes'}; cases.append(f)
        f=self.flow(); f['steps'][0]['choices']=[{'value':'yes','label':'One'},{'value':'yes','label':'Two'}]; cases.append(f)
        f=self.flow(); f['steps']=[]; cases.append(f)
        for flow in cases:
            with self.assertRaises(ValueError): build_guide.build(flow)

    def test_bridge_can_be_disabled(self):
        rendered=build_guide.build(self.flow(),False)
        self.assertIn('"hostBridge": false',rendered)

    def test_example(self):
        example=SCRIPT.parent.parent / 'assets' / 'branch-protection.json'
        self.assertGreater(len(build_guide.build(json.loads(example.read_text()))),1000)

if __name__ == '__main__': unittest.main()
