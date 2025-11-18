# Frontend Developer Interview - Mid-Senior Level

**Duration:** 45 minutes  
**Format:** Verbal Discussion + Live Coding Session

---

## Interview Structure

1. **Verbal Questions** (15 minutes)
2. **Live Coding Challenge** (30 minutes)

---

## Part 1: Verbal Questions (15 minutes)

### React Fundamentals & Best Practices

**Q1: Component Lifecycle & Hooks**
- Can you explain the difference between `useEffect` with an empty dependency array `[]` versus no dependency array at all?
- When would you use `useLayoutEffect` instead of `useEffect`? Can you provide a practical example?

**Q2: State Management**
- In a React application, when would you choose to use `useReducer` over `useState`? What are the trade-offs?
- How do you handle complex state updates that depend on previous state values? Can you walk me through your approach?

**Q3: Performance Optimization**
- What strategies do you use to optimize React component re-renders?
- Can you explain the concept of memoization in React? When would you use `React.memo`, `useMemo`, or `useCallback`?

**Q4: Component Architecture**
- How do you decide when to break down a component into smaller components?
- Can you describe a scenario where you've used the Compound Component pattern or Render Props pattern? What problem did it solve?

**Q5: TypeScript & Type Safety**
- How do you approach typing complex React components, especially when dealing with generic components or higher-order components?
- What's your strategy for handling type safety with event handlers and form inputs?

---

## Part 2: Live Coding Challenge (30 minutes)

### Task: Interactive Task Manager with Filtering & Search

You'll be building a **Task Manager** component that allows users to create, manage, and organize tasks with advanced filtering and search capabilities. This challenge will test your React skills, state management, and ability to create an interactive user experience.

#### Requirements

1. **Task Management**
   - Users should be able to add new tasks with:
     - A title (required)
     - An optional description
     - A priority level (Low, Medium, High)
     - A completion status (completed/incomplete)
   - Tasks should be editable (inline editing or edit mode)
   - Tasks should be deletable
   - Users should be able to toggle task completion status

2. **Filtering & Search**
   - Implement a search bar that filters tasks by title or description (real-time search)
   - Add filter buttons/options to filter by:
     - Priority level (show All, Low, Medium, or High priority tasks)
     - Completion status (show All, Completed, or Incomplete tasks)
   - Filters should work together (e.g., search + priority filter + status filter)

3. **Sorting**
   - Add ability to sort tasks by:
     - Priority (High → Low)
     - Creation order (newest first or oldest first)
   - Sorting should work in combination with filters

4. **State Management**
   - Manage all tasks and filter/search/sort states within the component
   - Ensure state updates are handled correctly and efficiently
   - Consider performance when filtering/searching large lists

5. **UI/UX Considerations**
   - Display task count (e.g., "5 tasks" or "3 of 5 tasks completed")
   - Show visual indicators for priority levels (colors, badges, etc.)
   - Make it visually appealing and intuitive
   - Add smooth transitions where appropriate
   - Ensure the interface is responsive

#### Technical Constraints

- Use React hooks (`useState`, `useEffect`, `useMemo`, `useCallback` as needed)
- TypeScript is required - ensure proper typing throughout
- Focus on clean, maintainable code and component composition
- You don't need to persist data (no backend required)
- Consider performance optimizations for filtering/searching

#### Evaluation Criteria

- **Code Quality**: Clean, readable, and well-structured code
- **React Best Practices**: Proper use of hooks, component composition, and state management
- **TypeScript**: Proper type definitions and type safety
- **Functionality**: All features work as expected and filters work together correctly
- **Performance**: Efficient filtering and searching (consider memoization)
- **User Experience**: Intuitive interface with good visual feedback
- **Problem-Solving**: How you approach and solve the challenge

#### Getting Started

1. The project is already set up with React, TypeScript, and Vite
2. Run `pnpm install` to install dependencies (if needed)
3. Run `pnpm dev` to start the development server
4. Start building in `src/App.tsx` or create new components as needed

#### Tips

- Start with the basic structure and add features incrementally
- Don't worry about making it perfect - focus on demonstrating your thought process
- Feel free to ask clarifying questions if anything is unclear
- We're interested in seeing how you think through problems, not just the final solution

---

## Notes for Interviewer

- Allow the candidate to think out loud and explain their approach
- Encourage questions and discussion during the coding session
- Focus on problem-solving skills and code quality over perfect implementation
- Be flexible with time allocation if the candidate needs more discussion or coding time

---

**Good luck! We're excited to see what you build! 🚀**
