# Backend Developer Interview - Mid-Senior Level (Python & FastAPI)

**Duration:** 30 minutes  
**Format:** Verbal Technical Discussion

---

## Interview Structure

This interview focuses on Python, FastAPI, async programming, background tasks, workers, and job queues. Questions are designed to assess deep technical knowledge and practical experience.

---

## Part 1: FastAPI & Async Programming (10 minutes)

### Q1: Async/Await Fundamentals
- Can you explain the difference between synchronous and asynchronous code execution in Python? When would you choose async over sync?
- In FastAPI, how does the event loop handle concurrent requests? What happens when you have blocking I/O operations in an async endpoint?
- What's the difference between `async def` and regular `def` in FastAPI? Can you give an example where using `async def` would actually hurt performance?

### Q2: FastAPI Advanced Patterns
- How does FastAPI's dependency injection system work? Can you explain a scenario where you'd use a dependency with `yield` instead of `return`?
- What are the differences between `BackgroundTasks`, `asyncio.create_task()`, and external task queues (like Celery)? When would you use each approach?
- How do you handle database connection pooling in FastAPI with async database drivers? What are common pitfalls?

### Q3: Error Handling & Middleware
- How would you implement global exception handling in FastAPI? What's the difference between exception handlers and middleware?
- Can you explain how FastAPI middleware works? How would you create middleware that measures request/response times?
- How do you handle database transaction rollbacks in async FastAPI endpoints? What happens if an exception occurs mid-transaction?

---

## Part 2: Background Tasks & Workers (10 minutes)

### Q4: Background Tasks Architecture
- When should you use FastAPI's `BackgroundTasks` versus a dedicated task queue like Celery or RQ? What are the trade-offs?
- Can you explain the difference between task queues and message brokers? How do they work together in a distributed system?
- What happens to background tasks if your FastAPI application crashes or restarts? How would you ensure task reliability?

### Q5: Celery & Distributed Workers
- How does Celery's task routing work? Can you explain the difference between direct, topic, and fanout exchanges?
- What are Celery task priorities and how do they work? How would you implement a priority queue for different types of jobs?
- How do you handle task retries and exponential backoff in Celery? What's the difference between `autoretry_for` and manual retry logic?
- Can you explain Celery's result backend? When would you use Redis vs RabbitMQ vs database as a result backend?

### Q6: Job Processing Patterns
- What's the difference between synchronous and asynchronous task execution in Celery? When would you use `task.delay()` vs `task.apply_async()`?
- How would you implement a job scheduler that runs periodic tasks (like cron jobs) using Celery Beat?
- How do you handle long-running tasks that might exceed Celery's default timeout? What strategies would you use?
- Can you explain task chaining, grouping, and callbacks in Celery? Provide a practical use case for each.

---

## Part 3: System Design & Best Practices (10 minutes)

### Q7: Scalability & Performance
- How would you design a system to handle 10,000 concurrent requests in FastAPI? What bottlenecks should you consider?
- How do you prevent memory leaks in long-running async applications? What are common sources of memory leaks in Python async code?
- How would you implement rate limiting in FastAPI? What's the difference between in-memory rate limiting and distributed rate limiting?

### Q8: Database & ORM Patterns
- How do you handle database migrations in a FastAPI application? What's your approach to managing schema changes?
- Can you explain the N+1 query problem in async ORMs like SQLAlchemy with async drivers? How would you solve it?
- How do you implement database connection retry logic and circuit breakers in async database operations?

### Q9: Testing & Debugging
- How do you test async FastAPI endpoints? What are the challenges with testing async code?
- How would you test background tasks and Celery workers? What mocking strategies would you use?
- How do you debug issues in distributed systems with multiple workers? What logging and monitoring strategies do you use?

### Q10: Production Considerations
- How do you handle graceful shutdown of FastAPI applications with pending background tasks?
- What's your strategy for monitoring and alerting on failed tasks in a production environment?
- How would you implement task deduplication to prevent duplicate job execution?
- Can you explain how you'd implement task result caching and when it's appropriate?

---

## Evaluation Criteria

- **Technical Depth**: Understanding of async/await, event loops, and concurrency models
- **Architecture Knowledge**: Ability to choose appropriate patterns (BackgroundTasks vs Celery vs asyncio)
- **Problem-Solving**: Practical solutions to real-world problems (reliability, scalability, error handling)
- **Best Practices**: Knowledge of production-ready patterns, monitoring, and debugging strategies
- **Communication**: Clear explanation of complex concepts

---

## Notes for Interviewer

- Focus on understanding the candidate's reasoning and trade-off analysis
- Encourage discussion about real-world scenarios and past experiences
- If the candidate mentions specific tools or patterns, dive deeper into their understanding
- Assess not just knowledge but also practical experience and problem-solving approach
- Be flexible with time - some questions may lead to deeper discussions

---

**Good luck! We're looking forward to our discussion! 🚀**

