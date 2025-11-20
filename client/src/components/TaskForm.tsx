import { useState } from "react";
import { Priority } from "../types";
import "./TaskForm.css";

interface TaskFormProps {
  onSubmit: (task: {
    title: string;
    description: string;
    priority: Priority;
    status: "incomplete";
  }) => void;
}

export default function TaskForm({ onSubmit }: TaskFormProps) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [priority, setPriority] = useState<Priority>("Medium");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (title.trim()) {
      onSubmit({
        title: title.trim(),
        description: description.trim(),
        priority,
        status: "incomplete",
      });
      setTitle("");
      setDescription("");
      setPriority("Medium");
    }
  };

  return (
    <form className="task-form" onSubmit={handleSubmit}>
      <div className="form-group">
        <input
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Task title *"
          className="form-input"
          required
        />
      </div>
      <div className="form-group">
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Description (optional)"
          className="form-textarea"
          rows={2}
        />
      </div>
      <div className="form-group form-row">
        <select
          value={priority}
          onChange={(e) => setPriority(e.target.value as Priority)}
          className="form-select"
        >
          <option value="Low">Low Priority</option>
          <option value="Medium">Medium Priority</option>
          <option value="High">High Priority</option>
        </select>
        <button type="submit" className="btn-add">
          Add Task
        </button>
      </div>
    </form>
  );
}
