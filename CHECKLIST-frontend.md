# Frontend Interview - Evaluation Checklist

**Candidate Name:** _______________________  
**Date:** _______________________  
**Interviewer:** _______________________

---

## Part 1: Verbal Questions (15 minutes)

### Q1: Component Lifecycle & Hooks

- [ ] Explains difference between `useEffect([])` vs `useEffect()` correctly
- [ ] Understands that `[]` runs once on mount, no array runs on every render
- [ ] Can explain `useLayoutEffect` vs `useEffect` difference
- [ ] Provides practical example for `useLayoutEffect` (e.g., DOM measurements)
- [ ] Shows understanding of cleanup functions in `useEffect`

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Q2: State Management

- [ ] Explains when to use `useReducer` vs `useState`
- [ ] Mentions complex state logic, multiple sub-values, or state transitions
- [ ] Understands trade-offs (more boilerplate vs better organization)
- [ ] Explains handling state updates that depend on previous state
- [ ] Mentions functional updates `setState(prev => ...)` or `useReducer`

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Q3: Performance Optimization

- [ ] Lists strategies for optimizing re-renders (memoization, keys, etc.)
- [ ] Explains `React.memo` correctly (shallow comparison)
- [ ] Explains `useMemo` correctly (memoize expensive computations)
- [ ] Explains `useCallback` correctly (memoize function references)
- [ ] Understands when NOT to use memoization (premature optimization)
- [ ] Mentions other optimization techniques (code splitting, lazy loading)

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Q4: Component Architecture

- [ ] Explains criteria for breaking down components (reusability, complexity, etc.)
- [ ] Describes Compound Component pattern correctly
- [ ] Describes Render Props pattern correctly
- [ ] Provides practical use case for one of these patterns
- [ ] Shows understanding of component composition

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Q5: TypeScript & Type Safety

- [ ] Explains typing generic components approach
- [ ] Understands typing HOCs (Higher Order Components)
- [ ] Explains typing event handlers correctly
- [ ] Explains typing form inputs correctly
- [ ] Mentions `React.ChangeEvent`, `React.FormEvent`, etc.
- [ ] Shows understanding of type inference and explicit typing trade-offs

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

## Part 2: Live Coding Challenge (30 minutes)

### Task Management Features

- [ ] Can add new tasks with title (required)
- [ ] Can add optional description
- [ ] Can set priority level (Low, Medium, High)
- [ ] Can set completion status
- [ ] Can edit tasks (inline or edit mode)
- [ ] Can delete tasks
- [ ] Can toggle completion status

**Code Quality:**
- [ ] Clean, readable code structure
- [ ] Proper component composition
- [ ] Good separation of concerns
- [ ] Meaningful variable/function names

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Filtering & Search

- [ ] Implements search bar that filters by title/description
- [ ] Search works in real-time (as user types)
- [ ] Can filter by priority level (All, Low, Medium, High)
- [ ] Can filter by completion status (All, Completed, Incomplete)
- [ ] Multiple filters work together correctly
- [ ] Search + priority + status filters combine properly

**Implementation:**
- [ ] Uses appropriate state management for filters
- [ ] Efficient filtering logic
- [ ] Considered performance (memoization if needed)

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Sorting

- [ ] Can sort by priority (High → Low)
- [ ] Can sort by creation order (newest/oldest first)
- [ ] Sorting works with filters applied
- [ ] Sorting state is managed properly

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### State Management

- [ ] Properly manages all task state
- [ ] Properly manages filter/search/sort state
- [ ] State updates are handled correctly
- [ ] Uses appropriate hooks (`useState`, `useMemo`, `useCallback`)
- [ ] No unnecessary re-renders
- [ ] Efficient state structure

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### TypeScript

- [ ] Proper type definitions for tasks
- [ ] Proper typing for state
- [ ] Proper typing for event handlers
- [ ] Proper typing for functions/props
- [ ] No `any` types (or justified use)
- [ ] Type safety throughout

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### UI/UX

- [ ] Displays task count
- [ ] Shows visual indicators for priority (colors/badges)
- [ ] Visually appealing interface
- [ ] Smooth transitions/animations
- [ ] Responsive design considerations
- [ ] Intuitive user experience
- [ ] Good visual feedback

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Problem-Solving Approach

- [ ] Asks clarifying questions when needed
- [ ] Breaks down problem into smaller parts
- [ ] Implements features incrementally
- [ ] Thinks out loud and explains approach
- [ ] Handles edge cases
- [ ] Debugs effectively when issues arise

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

## Overall Assessment

### Technical Skills
- [ ] Excellent (4/4)
- [ ] Good (3/4)
- [ ] Satisfactory (2/4)
- [ ] Needs Improvement (1/4)

### Code Quality
- [ ] Excellent (4/4)
- [ ] Good (3/4)
- [ ] Satisfactory (2/4)
- [ ] Needs Improvement (1/4)

### Problem-Solving
- [ ] Excellent (4/4)
- [ ] Good (3/4)
- [ ] Satisfactory (2/4)
- [ ] Needs Improvement (1/4)

### Communication
- [ ] Excellent (4/4)
- [ ] Good (3/4)
- [ ] Satisfactory (2/4)
- [ ] Needs Improvement (1/4)

---

## Final Notes & Recommendation

**Strengths:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

**Areas for Improvement:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

**Overall Recommendation:**
- [ ] Strong Hire
- [ ] Hire
- [ ] Maybe / Needs More Evaluation
- [ ] No Hire

**Additional Comments:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

