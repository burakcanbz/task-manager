import { useState, useMemo, useCallback } from 'react';
import './App.css';
import { Task, Priority, PriorityFilter, StatusFilter, SortOption } from './types';
import TaskItem from './components/TaskItem';
import TaskForm from './components/TaskForm';
import FilterBar from './components/FilterBar';

// Initial demo tasks
const getInitialTasks = (): Task[] => {
  const now = Date.now();
  const tasks: Task[] = [
    {
      id: '1',
      title: 'Complete project documentation',
      description: 'Write comprehensive documentation for the task manager application including API endpoints and user guide',
      priority: 'High',
      status: 'incomplete',
      createdAt: now - 86400000 * 2, // 2 days ago
    },
    {
      id: '2',
      title: 'Review code changes',
      description: 'Review pull requests from team members and provide feedback',
      priority: 'High',
      status: 'completed',
      createdAt: now - 86400000 * 1, // 1 day ago
    },
    {
      id: '3',
      title: 'Update dependencies',
      description: 'Check and update npm packages to latest stable versions',
      priority: 'Medium',
      status: 'incomplete',
      createdAt: now - 86400000 * 3, // 3 days ago
    },
    {
      id: '4',
      title: 'Design new UI components',
      description: 'Create mockups for the new dashboard interface',
      priority: 'Medium',
      status: 'incomplete',
      createdAt: now - 86400000 * 4, // 4 days ago
    },
    {
      id: '5',
      title: 'Fix bug in filter functionality',
      description: 'Investigate and fix the issue with search filter not working correctly',
      priority: 'High',
      status: 'completed',
      createdAt: now - 86400000 * 5, // 5 days ago
    },
    {
      id: '6',
      title: 'Write unit tests',
      description: 'Add unit tests for task management functions',
      priority: 'Medium',
      status: 'incomplete',
      createdAt: now - 86400000 * 6, // 6 days ago
    },
    {
      id: '7',
      title: 'Organize team meeting',
      description: 'Schedule and prepare agenda for weekly team sync',
      priority: 'Low',
      status: 'completed',
      createdAt: now - 86400000 * 7, // 7 days ago
    },
    {
      id: '8',
      title: 'Optimize database queries',
      description: 'Review and optimize slow database queries in the backend',
      priority: 'High',
      status: 'incomplete',
      createdAt: now - 86400000 * 8, // 8 days ago
    },
    {
      id: '9',
      title: 'Update README file',
      description: 'Add installation and usage instructions to README',
      priority: 'Low',
      status: 'incomplete',
      createdAt: now - 86400000 * 9, // 9 days ago
    },
    {
      id: '10',
      title: 'Implement dark mode',
      description: 'Add dark mode theme toggle to the application',
      priority: 'Medium',
      status: 'completed',
      createdAt: now - 86400000 * 10, // 10 days ago
    },
    {
      id: '11',
      title: 'Set up CI/CD pipeline',
      description: 'Configure GitHub Actions for automated testing and deployment',
      priority: 'High',
      status: 'incomplete',
      createdAt: now - 86400000 * 11, // 11 days ago
    },
    {
      id: '12',
      title: 'Refactor authentication module',
      description: 'Improve code structure and security of authentication system',
      priority: 'Medium',
      status: 'incomplete',
      createdAt: now - 86400000 * 12, // 12 days ago
    },
    {
      id: '13',
      title: 'Create user onboarding flow',
      description: 'Design and implement welcome screens for new users',
      priority: 'Low',
      status: 'completed',
      createdAt: now - 86400000 * 13, // 13 days ago
    },
    {
      id: '14',
      title: 'Add error logging',
      description: 'Implement comprehensive error logging and monitoring',
      priority: 'Medium',
      status: 'incomplete',
      createdAt: now - 86400000 * 14, // 14 days ago
    },
    {
      id: '15',
      title: 'Performance testing',
      description: 'Run load tests and identify performance bottlenecks',
      priority: 'High',
      status: 'incomplete',
      createdAt: now - 86400000 * 15, // 15 days ago
    },
    {
      id: '16',
      title: 'Update user documentation',
      description: 'Create video tutorials for common user workflows',
      priority: 'Low',
      status: 'incomplete',
      createdAt: now - 86400000 * 16, // 16 days ago
    },
    {
      id: '17',
      title: 'Implement search suggestions',
      description: 'Add autocomplete functionality to search bar',
      priority: 'Medium',
      status: 'completed',
      createdAt: now - 86400000 * 17, // 17 days ago
    },
    {
      id: '18',
      title: 'Security audit',
      description: 'Conduct security review and fix vulnerabilities',
      priority: 'High',
      status: 'incomplete',
      createdAt: now - 86400000 * 18, // 18 days ago
    },
  ];
  return tasks;
};

function App() {
  const [tasks, setTasks] = useState<Task[]>(getInitialTasks());
  const [searchQuery, setSearchQuery] = useState('');
  const [priorityFilter, setPriorityFilter] = useState<PriorityFilter>('All');
  const [statusFilter, setStatusFilter] = useState<StatusFilter>('All');
  const [sortOption, setSortOption] = useState<SortOption>('newest');
  const [editingTaskId, setEditingTaskId] = useState<string | null>(null);

  const addTask = useCallback((task: Omit<Task, 'id' | 'createdAt'>) => {
    const newTask: Task = {
      ...task,
      id: Date.now().toString(),
      createdAt: Date.now(),
    };
    setTasks((prev) => [...prev, newTask]);
  }, []);

  const updateTask = useCallback((id: string, updates: Partial<Task>) => {
    setTasks((prev) =>
      prev.map((task) => (task.id === id ? { ...task, ...updates } : task))
    );
    setEditingTaskId(null);
  }, []);

  const deleteTask = useCallback((id: string) => {
    setTasks((prev) => prev.filter((task) => task.id !== id));
  }, []);

  const toggleTaskStatus = useCallback((id: string) => {
    setTasks((prev) =>
      prev.map((task) =>
        task.id === id
          ? {
              ...task,
              status: task.status === 'completed' ? 'incomplete' : 'completed',
            }
          : task
      )
    );
  }, []);

  const filteredAndSortedTasks = useMemo(() => {
    let filtered = tasks.filter((task) => {
      // Search filter
      const matchesSearch =
        searchQuery === '' ||
        task.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        task.description.toLowerCase().includes(searchQuery.toLowerCase());

      // Priority filter
      const matchesPriority =
        priorityFilter === 'All' || task.priority === priorityFilter;

      // Status filter
      const matchesStatus =
        statusFilter === 'All' ||
        (statusFilter === 'Completed' && task.status === 'completed') ||
        (statusFilter === 'Incomplete' && task.status === 'incomplete');

      return matchesSearch && matchesPriority && matchesStatus;
    });

    // Sorting
    const sorted = [...filtered].sort((a, b) => {
      if (sortOption === 'priority') {
        const priorityOrder: Record<Priority, number> = {
          High: 3,
          Medium: 2,
          Low: 1,
        };
        return priorityOrder[b.priority] - priorityOrder[a.priority];
      } else if (sortOption === 'newest') {
        return b.createdAt - a.createdAt;
      } else {
        return a.createdAt - b.createdAt;
      }
    });

    return sorted;
  }, [tasks, searchQuery, priorityFilter, statusFilter, sortOption]);

  const completedCount = useMemo(
    () => tasks.filter((task) => task.status === 'completed').length,
    [tasks]
  );

  const totalCount = tasks.length;

  return (
    <div className="app">
      <header className="app-header">
        <h1>Task Manager</h1>
        <div className="task-stats">
          {totalCount > 0 ? (
            <span>
              {completedCount} of {totalCount} tasks completed
            </span>
          ) : (
            <span>No tasks yet</span>
          )}
        </div>
      </header>

      <main className="app-main">
        <TaskForm onSubmit={addTask} />

        <FilterBar
          searchQuery={searchQuery}
          onSearchChange={setSearchQuery}
          priorityFilter={priorityFilter}
          onPriorityFilterChange={setPriorityFilter}
          statusFilter={statusFilter}
          onStatusFilterChange={setStatusFilter}
          sortOption={sortOption}
          onSortChange={setSortOption}
        />

        <div className="tasks-container">
          {filteredAndSortedTasks.length === 0 ? (
            <div className="empty-state">
              <p>
                {tasks.length === 0
                  ? 'No tasks yet. Add your first task above!'
                  : 'No tasks match your filters. Try adjusting your search or filters.'}
              </p>
            </div>
          ) : (
            <ul className="task-list">
              {filteredAndSortedTasks.map((task) => (
                <TaskItem
                  key={task.id}
                  task={task}
                  isEditing={editingTaskId === task.id}
                  onEdit={() => setEditingTaskId(task.id)}
                  onCancelEdit={() => setEditingTaskId(null)}
                  onUpdate={(updates) => updateTask(task.id, updates)}
                  onDelete={() => deleteTask(task.id)}
                  onToggleStatus={() => toggleTaskStatus(task.id)}
                />
              ))}
            </ul>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
