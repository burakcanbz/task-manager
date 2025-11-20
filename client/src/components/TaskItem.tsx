import { useState, useEffect } from 'react';
import { Task, Priority } from '../types';
import './TaskItem.css';

interface TaskItemProps {
  task: Task;
  isEditing: boolean;
  onEdit: () => void;
  onCancelEdit: () => void;
  onUpdate: (updates: Partial<Task>) => void;
  onDelete: () => void;
  onToggleStatus: () => void;
}

const priorityColors: Record<Priority, string> = {
  Low: '#4caf50',
  Medium: '#ff9800',
  High: '#f44336',
};

export default function TaskItem({
  task,
  isEditing,
  onEdit,
  onCancelEdit,
  onUpdate,
  onDelete,
  onToggleStatus,
}: TaskItemProps) {
  const [title, setTitle] = useState(task.title);
  const [description, setDescription] = useState(task.description);
  const [priority, setPriority] = useState<Priority>(task.priority);

  useEffect(() => {
    if (isEditing) {
      setTitle(task.title);
      setDescription(task.description);
      setPriority(task.priority);
    }
  }, [isEditing, task]);

  const handleSave = () => {
    if (title.trim()) {
      onUpdate({ title: title.trim(), description: description.trim(), priority });
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && (e.ctrlKey || e.metaKey)) {
      handleSave();
    } else if (e.key === 'Escape') {
      onCancelEdit();
    }
  };

  return (
    <li className={`task-item ${task.status === 'completed' ? 'completed' : ''}`}>
      <div className="task-checkbox">
        <input
          type="checkbox"
          checked={task.status === 'completed'}
          onChange={onToggleStatus}
          aria-label="Toggle task completion"
        />
      </div>

      {isEditing ? (
        <div className="task-edit-form" onKeyDown={handleKeyDown}>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Task title"
            className="task-edit-title"
            autoFocus
          />
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Description (optional)"
            className="task-edit-description"
            rows={2}
          />
          <select
            value={priority}
            onChange={(e) => setPriority(e.target.value as Priority)}
            className="task-edit-priority"
          >
            <option value="Low">Low</option>
            <option value="Medium">Medium</option>
            <option value="High">High</option>
          </select>
          <div className="task-edit-actions">
            <button onClick={handleSave} className="btn-save">
              Save (Ctrl+Enter)
            </button>
            <button onClick={onCancelEdit} className="btn-cancel">
              Cancel (Esc)
            </button>
          </div>
        </div>
      ) : (
        <div className="task-content">
          <div className="task-header">
            <h3 className="task-title">{task.title}</h3>
            <span
              className="task-priority-badge"
              style={{ backgroundColor: priorityColors[task.priority] }}
            >
              {task.priority}
            </span>
          </div>
          {task.description && (
            <p className="task-description">{task.description}</p>
          )}
          <div className="task-actions">
            <button onClick={onEdit} className="btn-edit" disabled={task.status === "completed"}>
              Edit
            </button>
            <button onClick={onDelete} className="btn-delete"  disabled={task.status === "completed"}>
              Delete
            </button>
          </div>
        </div>
      )}
    </li>
  );
}

