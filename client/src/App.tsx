import { useState, useMemo, useCallback, useEffect } from "react";
import "./App.css";
import {
  Task,
  Priority,
  PriorityFilter,
  StatusFilter,
  SortOption,
} from "./types";
import TaskItem from "./components/TaskItem";
import TaskForm from "./components/TaskForm";
import FilterBar from "./components/FilterBar";
import axios from "axios";
import { BASE_URL } from "./api/endpoints";

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState("");
  const [priorityFilter, setPriorityFilter] = useState<PriorityFilter>("All");
  const [statusFilter, setStatusFilter] = useState<StatusFilter>("All");
  const [sortOption, setSortOption] = useState<SortOption>("newest");
  const [editingTaskId, setEditingTaskId] = useState<string | null>(null);

  const addTask = useCallback(
    async (task: Omit<Task, "id" | "createdAt" | "updatedAt">) => {
      try {
        const response = await axios.post<Task>(`${BASE_URL}`, task);

        // backend yeni id ve timestamps ile task döndü
        const newTask = response.data;

        setTasks((prev) => [...prev, newTask]); // UI güncellenir → re-render tetiklenir
      } catch (err) {
        console.error(err);
      }
    },
    []
  );

  const updateTask = useCallback(async (id: string, updates: Partial<Task>) => {
    try {
      const taskToUpdate = {
        ...updates,
        status: updates.status ?? tasks.find((t) => t.id === id)?.status,
      };

      const resp = await axios.put(`${BASE_URL}/${id}`, taskToUpdate);
      const updatedTask: Task = resp.data;

      setTasks((prev) =>
        prev.map((task) => (task.id === id ? updatedTask : task))
      );
    } catch (err) {
      console.error("Failed to update task:", err);
    } finally {
      setEditingTaskId(null);
    }
  }, []);

  const deleteTask = useCallback(async (id: string) => {
    try {
      await axios.delete(`${BASE_URL}/${id}`);
      setTasks((prev) => prev.filter((task) => task.id !== id));
    } catch (err) {
      console.error("Failed to update task:", err);
    }
  }, []);

  const toggleTaskStatus = useCallback((id: string) => {
    setTasks((prev) =>
      prev.map((task) =>
        task.id === id
          ? {
            ...task,
            status: task.status === "completed" ? "incomplete" : "completed",
          }
          : task
      )
    );
  }, []);

  const filteredAndSortedTasks = useMemo(() => {
    let filtered = tasks.filter((task) => {
      // Search filter
      const matchesSearch =
        searchQuery === "" ||
        task.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        task.description.toLowerCase().includes(searchQuery.toLowerCase());

      // Priority filter
      const matchesPriority =
        priorityFilter === "All" || task.priority === priorityFilter;

      // Status filter
      const matchesStatus =
        statusFilter === "All" ||
        (statusFilter === "Completed" && task.status === "completed") ||
        (statusFilter === "Incomplete" && task.status === "incomplete");

      return matchesSearch && matchesPriority && matchesStatus;
    });

    // Sorting
    const sorted = [...filtered].sort((a, b) => {
      if (sortOption === "priority") {
        const priorityOrder: Record<Priority, number> = {
          High: 3,
          Medium: 2,
          Low: 1,
        };
        return priorityOrder[b.priority] - priorityOrder[a.priority];
      } else if (sortOption === "newest") {
        return (
          new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime()
        );
      } else {
        return (
          new Date(a.createdAt).getTime() - new Date(b.createdAt).getTime()
        );
      }
    });

    return sorted;
  }, [tasks, searchQuery, priorityFilter, statusFilter, sortOption]);

  const completedCount = useMemo(
    () => tasks.filter((task) => task.status === "completed").length,
    [tasks]
  );

  const totalCount = tasks.length;

  useEffect(() => {
    const fetchTasks = async () => {
      try {
        const resp = await axios.get<Task[]>(BASE_URL);
        setTasks(resp.data);
      } catch (err) {
        console.error("Error fetching tasks:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, []);

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
            <div className="empty-state" style={{ display: "flex", justifyContent: "center", alignItems: "center" }}>
              <div>
                {tasks.length === 0
                  ? <div className="loader"></div>
                  : "No tasks match your filters. Try adjusting your search or filters."}
              </div>
            </div>
          ) : (
            <ul className="task-list">
              {filteredAndSortedTasks.map((task) => {
                return (
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
                );
              })}
            </ul>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;
