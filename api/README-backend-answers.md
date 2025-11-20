# Backend Developer Interview - Answers & Evaluation Guide

**Note:** This file contains sample answers and evaluation criteria for the backend interview questions.

---

## Part 1: FastAPI & Async Programming

### Q1: Async/Await Fundamentals

**Expected Understanding:**
- Async code allows concurrent execution without blocking the event loop
- FastAPI uses ASGI (Asynchronous Server Gateway Interface) which runs on an event loop
- Blocking I/O in async endpoints defeats the purpose - should use `run_in_executor` or sync endpoints
- `async def` adds overhead; use only when there's actual async I/O

**Key Points to Look For:**
- Understanding of event loop and how it handles concurrent requests
- Knowledge that async doesn't automatically mean faster - only beneficial for I/O-bound operations
- Awareness of GIL limitations in CPU-bound tasks

**Sample Answer Highlights:**
- Async allows non-blocking I/O operations, enabling handling multiple requests concurrently
- FastAPI's event loop can handle thousands of concurrent connections
- Blocking operations (like CPU-intensive tasks) should use thread pools or sync endpoints
- `async def` adds coroutine overhead; unnecessary use can hurt performance

---

### Q2: FastAPI Advanced Patterns

**Expected Understanding:**
- Dependency injection allows code reuse and testability
- Dependencies with `yield` are used for setup/teardown (like database connections)
- `BackgroundTasks` are simple but limited (no retry, no persistence)
- `asyncio.create_task()` is for fire-and-forget async tasks
- External queues (Celery) are for complex, distributed, reliable task processing

**Key Points to Look For:**
- Understanding of dependency lifecycle (init → yield → cleanup)
- Clear distinction between different async task approaches
- Knowledge of when to use each pattern

**Sample Answer Highlights:**
- Dependencies with `yield` are perfect for database connections, file handles, etc.
- `BackgroundTasks`: Simple, in-process, lost on restart
- `asyncio.create_task()`: Async fire-and-forget, no persistence
- Celery: Distributed, persistent, retryable, scalable

---

### Q3: Error Handling & Middleware

**Expected Understanding:**
- Exception handlers catch specific exceptions and return responses
- Middleware intercepts requests/responses and can modify them
- Database transactions need proper rollback handling
- Context managers or try/except/finally for transaction management

**Key Points to Look For:**
- Understanding of exception handler vs middleware distinction
- Proper transaction management patterns
- Knowledge of async context managers

**Sample Answer Highlights:**
- Exception handlers: `@app.exception_handler(Exception)` - handle specific errors
- Middleware: Runs before/after request processing, can modify requests/responses
- Use async context managers or explicit commit/rollback for transactions
- Ensure rollback happens even if exceptions occur mid-transaction

---

## Part 2: Background Tasks & Workers

### Q4: Background Tasks Architecture

**Expected Understanding:**
- `BackgroundTasks`: Simple, in-process, lost on restart
- Task queues: Distributed, persistent, retryable
- Message brokers: Transport layer (RabbitMQ, Redis, etc.)
- Task queues use message brokers for communication

**Key Points to Look For:**
- Clear understanding of when to use BackgroundTasks vs Celery
- Knowledge of message broker role
- Understanding of task persistence and reliability

**Sample Answer Highlights:**
- BackgroundTasks: Quick tasks, no persistence needed, simple use cases
- Celery: Long-running, need retry, distributed, need persistence
- Message brokers transport messages; task queues manage job lifecycle
- Tasks lost on crash unless using persistent queue

---

### Q5: Celery & Distributed Workers

**Expected Understanding:**
- Direct exchange: Routing key matches queue name exactly
- Topic exchange: Pattern matching on routing keys
- Fanout exchange: Broadcasts to all queues
- Task priorities: Higher priority tasks processed first
- Result backends: Store task results (Redis, database, etc.)

**Key Points to Look For:**
- Deep understanding of Celery architecture
- Knowledge of different exchange types
- Understanding of retry strategies and backoff
- Result backend selection criteria

**Sample Answer Highlights:**
- Direct: Exact match (e.g., `task_queue`)
- Topic: Pattern match (e.g., `*.email`, `user.*`)
- Fanout: Broadcast to all bound queues
- Priorities: 0-9, higher = more priority
- `autoretry_for`: Automatic retry on specific exceptions
- Manual retry: More control, custom logic
- Redis: Fast, ephemeral results
- Database: Persistent, queryable results
- RabbitMQ: Can be broker and result backend

---

### Q6: Job Processing Patterns

**Expected Understanding:**
- `delay()`: Synchronous call, returns AsyncResult
- `apply_async()`: More control (countdown, eta, priority, etc.)
- Celery Beat: Periodic task scheduler
- Task chaining: Sequential execution
- Grouping: Parallel execution
- Callbacks: Execute after task completion

**Key Points to Look For:**
- Understanding of task execution methods
- Knowledge of scheduling patterns
- Understanding of task composition

**Sample Answer Highlights:**
- `delay()`: Simple, `task.delay(arg1, arg2)`
- `apply_async()`: Advanced, `task.apply_async(args, countdown=60, priority=5)`
- Celery Beat: Cron-like scheduling, uses `beat_schedule`
- Long-running tasks: Increase `task_time_limit`, use `task_acks_late=True`
- Chaining: `chain(task1.s(), task2.s(), task3.s())`
- Grouping: `group(task1.s(i) for i in range(10))`
- Callbacks: `task.apply_async(callback=other_task.s())`

---

## Part 3: System Design & Best Practices

### Q7: Scalability & Performance

**Expected Understanding:**
- Connection pooling for databases
- Rate limiting strategies
- Caching strategies
- Load balancing considerations
- Database query optimization

**Key Points to Look For:**
- Understanding of scalability bottlenecks
- Knowledge of rate limiting approaches
- Memory management awareness

**Sample Answer Highlights:**
- Connection pooling: Reuse connections, limit pool size
- Rate limiting: Token bucket, sliding window, distributed (Redis)
- Memory leaks: Unclosed connections, circular references, event listeners
- Use `asyncio.gather()` for concurrent async operations
- Monitor connection pool usage and adjust accordingly

---

### Q8: Database & ORM Patterns

**Expected Understanding:**
- Alembic for migrations
- N+1 query problem and solutions (eager loading, select_related)
- Connection retry logic
- Circuit breakers for resilience

**Key Points to Look For:**
- Migration strategy knowledge
- Understanding of ORM performance issues
- Resilience patterns

**Sample Answer Highlights:**
- Alembic: Version control for database schema
- N+1: Use `joinedload()`, `selectinload()`, or `select_related()`
- Retry logic: Exponential backoff, max retries
- Circuit breaker: Fail fast when service is down, prevent cascade failures

---

### Q9: Testing & Debugging

**Expected Understanding:**
- `TestClient` for FastAPI testing
- `pytest-asyncio` for async tests
- Mocking Celery tasks
- Distributed tracing and logging

**Key Points to Look For:**
- Testing async code knowledge
- Mocking strategies
- Debugging distributed systems

**Sample Answer Highlights:**
- Use `TestClient` from `fastapi.testing`
- `pytest-asyncio` for async test functions
- Mock Celery: `@patch('module.celery_app')` or use `CELERY_TASK_ALWAYS_EAGER=True`
- Logging: Structured logging, correlation IDs, distributed tracing (OpenTelemetry)
- Monitoring: Task success/failure rates, execution times, queue depths

---

### Q10: Production Considerations

**Expected Understanding:**
- Graceful shutdown handling
- Monitoring and alerting
- Task deduplication
- Result caching strategies

**Key Points to Look For:**
- Production readiness awareness
- Monitoring strategies
- Optimization techniques

**Sample Answer Highlights:**
- Graceful shutdown: Handle SIGTERM, wait for pending tasks, close connections
- Monitoring: Prometheus metrics, Grafana dashboards, alert on failure rates
- Deduplication: Task IDs, Redis locks, idempotency keys
- Caching: Cache expensive computations, use TTL, invalidate on updates
- Use task result expiration for non-critical results

---

## Evaluation Rubric

### Excellent (4/4)
- Demonstrates deep understanding of async/await and event loops
- Can explain trade-offs between different approaches
- Shows production experience with real-world examples
- Understands scalability and reliability concerns

### Good (3/4)
- Solid understanding of core concepts
- Can explain most patterns correctly
- Some gaps in advanced topics
- Limited production experience

### Satisfactory (2/4)
- Basic understanding of async programming
- Can explain simple patterns
- Needs guidance on advanced topics
- Limited practical experience

### Needs Improvement (1/4)
- Surface-level understanding
- Struggles with core concepts
- Cannot explain trade-offs
- No production experience

---

## Additional Discussion Points

- Ask about specific projects they've worked on
- Discuss challenges they've faced with async/background tasks
- Explore their approach to debugging production issues
- Discuss their experience with monitoring and observability
- Ask about their preferred tools and why

---

**Remember:** The goal is to assess understanding, not to catch them off guard. Encourage discussion and real-world examples.

