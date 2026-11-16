const assert = require('node:assert/strict');
const {createGuideMachine} = require('../../assets/wizard-state.js');
const flow = {steps:[
  {id:'platform',choices:[{value:'mac'},{value:'win'}]},
  {id:'mac',showIf:{step:'platform',equals:'mac'}},
  {id:'win',showIf:{step:'platform',equals:'win'}},
  {id:'check'}
]};
const m = createGuideMachine(flow);
assert.deepEqual(m.snapshot().completed, []);
assert.equal(m.back(), false);
assert.equal(m.next(), false, 'choice required');
assert.equal(m.choose('invalid'), false);
m.choose('mac'); m.next();
assert.equal(m.current().id, 'mac');
assert.deepEqual(m.snapshot().completed, ['platform']);
m.back();
assert.equal(m.snapshot().answers.platform, 'mac');
assert.equal(m.choose('mac'), false, 'same selection does not invalidate');
m.next(); m.next();
assert.equal(m.current().id, 'check');
assert.equal(m.snapshot().done, false, 'visiting final step is not completion');
m.next(); assert.equal(m.snapshot().done, true);
m.review(); assert.equal(m.current().id, 'platform');
m.choose('win');
assert.deepEqual(m.snapshot().completed, [], 'changed choice clears all dependent completions');
assert.equal(m.snapshot().done, false);
assert.deepEqual(m.visible().map(s=>s.id), ['platform','win','check']);
m.next(); assert.equal(m.current().id,'win');
const restored=createGuideMachine(flow,m.snapshot());
assert.deepEqual(restored.snapshot(),m.snapshot());
restored.restore({current:'check', completed:['check'], answers:{platform:'win'}});
assert.equal(restored.current().id,'platform','restore cannot skip unconfirmed prerequisites');
assert.deepEqual(restored.snapshot().completed,[]);
restored.restore({current:'mac', completed:['platform','mac'], answers:{platform:'win'}, done:true});
assert.equal(restored.current().id,'win');
assert.equal(restored.snapshot().done,false,'hidden or stale branch cannot complete guide');
const single=createGuideMachine({steps:[{id:'only'}]});
assert.equal(single.next(),true); assert.equal(single.snapshot().done,true);
const nested=createGuideMachine({steps:[{id:'a',choices:[{value:'yes'},{value:'no'}]},{id:'b',showIf:{step:'a',equals:'yes'},choices:[{value:'one'},{value:'two'}]},{id:'c',showIf:{step:'b',equals:'one'}},{id:'end'}]}, {answers:{a:'no',b:'one'},completed:[]});
assert.deepEqual(nested.visible().map(s=>s.id),['a','end']);
assert.equal(nested.snapshot().answers.b,undefined);
console.log('State transitions passed: choice gating, Back, Done, branching, invalidation, restore, hidden ancestors.');
const {createGuideSync} = require('../../assets/wizard-state.js');
const sync = createGuideSync({sequence:4,writer:'old-view'},'current-view');
assert.equal(sync.accept({sequence:3,writer:'old-view'}),false,'ignore delayed older snapshot');
assert.equal(sync.accept({sequence:5,writer:'old-view'}),true,'restore newer state before local interaction');
assert.deepEqual(sync.local(),{sequence:6,writer:'current-view'});
assert.equal(sync.accept({sequence:6,writer:'current-view'}),false,'ignore own optimistic echo');
assert.equal(sync.accept({sequence:100,writer:'other-view'}),false,'local interaction cannot be overwritten by another writer');
assert.equal(sync.accept({sequence:5,writer:'old-view'}),false,'delayed old Done must not erase a changed choice');
console.log('Host state ordering passed: monotonic snapshots, echo suppression, local interaction wins.');
