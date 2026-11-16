/* Pure state transitions, shared by the renderer and navigation tests. */
function createGuideMachine(flow, restored) {
  const steps = flow.steps;
  let state = { current: steps[0].id, answers: {}, completed: [], visited: [steps[0].id], done: false };
  const own = (obj, key) => Object.prototype.hasOwnProperty.call(obj, key);
  const visible = () => {
    const shown = new Set();
    return steps.filter(step => {
      const ok = !step.showIf || (shown.has(step.showIf.step) && state.answers[step.showIf.step] === step.showIf.equals);
      if (ok) shown.add(step.id);
      return ok;
    });
  };
  function restore(saved) {
    state = { current: steps[0].id, answers: {}, completed: [], visited: [steps[0].id], done: false };
    if (!saved || typeof saved !== 'object') return;
    for (const step of steps) {
      if (step.choices && saved.answers && own(saved.answers, step.id) && step.choices.some(choice => choice.value === saved.answers[step.id])) {
        state.answers[step.id] = saved.answers[step.id];
      }
    }
    const shown = visible();
    const ids = new Set(shown.map(step => step.id));
    Object.keys(state.answers).forEach(id => { if (!ids.has(id)) delete state.answers[id]; });
    for (const step of shown) {
      if (!Array.isArray(saved.completed) || !saved.completed.includes(step.id) || (step.choices && !own(state.answers, step.id))) break;
      state.completed.push(step.id);
    }
    const firstUnfinished = shown.findIndex(step => !state.completed.includes(step.id));
    const requested = shown.findIndex(step => step.id === saved.current);
    const limit = firstUnfinished < 0 ? shown.length - 1 : firstUnfinished;
    state.current = shown[requested >= 0 ? Math.min(requested, limit) : limit].id;
    state.visited = Array.isArray(saved.visited) ? saved.visited.filter(id => ids.has(id)) : [];
    if (!state.visited.includes(state.current)) state.visited.push(state.current);
    state.done = saved.done === true && firstUnfinished < 0;
  }
  function snapshot() { return JSON.parse(JSON.stringify(state)); }
  function current() { return steps.find(step => step.id === state.current); }
  function move(id) {
    state.current = id;
    if (!state.visited.includes(id)) state.visited.push(id);
  }
  function choose(value) {
    const step = current();
    if (!step.choices || !step.choices.some(choice => choice.value === value)) return false;
    if (state.answers[step.id] === value) return false;
    const index = steps.findIndex(item => item.id === step.id);
    const later = new Set(steps.slice(index).map(item => item.id));
    Object.keys(state.answers).forEach(id => { if (later.has(id)) delete state.answers[id]; });
    state.completed = state.completed.filter(id => !later.has(id));
    state.visited = state.visited.filter(id => !later.has(id) || id === step.id);
    state.answers[step.id] = value;
    state.done = false;
    return true;
  }
  function next() {
    const step = current();
    if (step.choices && !own(state.answers, step.id)) return false;
    if (!state.completed.includes(step.id)) state.completed.push(step.id);
    const shown = visible();
    const index = shown.findIndex(item => item.id === step.id);
    if (index === shown.length - 1) state.done = true;
    else move(shown[index + 1].id);
    return true;
  }
  function back() {
    const shown = visible();
    const index = shown.findIndex(item => item.id === state.current);
    if (index <= 0) return false;
    state.done = false;
    move(shown[index - 1].id);
    return true;
  }
  function review() { state.done = false; move(visible()[0].id); }
  restore(restored);
  return { snapshot, visible, current, choose, next, back, review, restore };
}
/* Host snapshots are optimistic and may arrive out of order. Local edits win
   for the lifetime of this view; reopening can restore its saved snapshot. */
function createGuideSync(saved, writer) {
  let sequence = Number.isSafeInteger(saved?.sequence) && saved.sequence >= 0 ? saved.sequence : 0;
  let edited = false;
  return {
    local() { edited = true; sequence += 1; return { sequence, writer }; },
    accept(snapshot) {
      if (!snapshot || edited || snapshot.writer === writer || !Number.isSafeInteger(snapshot.sequence) || snapshot.sequence <= sequence) return false;
      sequence = snapshot.sequence;
      return true;
    }
  };
}
if (typeof module !== 'undefined' && module.exports) module.exports = { createGuideMachine, createGuideSync };
