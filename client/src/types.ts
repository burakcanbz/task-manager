export type Priority = 'Low' | 'Medium' | 'High';

export type TaskStatus = 'completed' | 'incomplete';

export type SortOption = 'priority' | 'newest' | 'oldest';

export interface Task {
  id: string;
  title: string;
  description: string;
  priority: Priority;
  status: TaskStatus;
  createdAt: number;
  updatedAt: number;
}

export type PriorityFilter = 'All' | Priority;

export type StatusFilter = 'All' | 'Completed' | 'Incomplete';

