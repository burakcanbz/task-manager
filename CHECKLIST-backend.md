# Backend Interview - Evaluation Checklist

**Candidate Name:** _______________________  
**Date:** _______________________  
**Interviewer:** _______________________

---

## Part 1: FastAPI & Async Programming (10 minutes)

### Q1: Async/Await Fundamentals

- [ ] Explains difference between sync and async code execution
- [ ] Understands when to choose async over sync (I/O-bound operations)
- [ ] Explains how FastAPI event loop handles concurrent requests
- [ ] Understands that blocking I/O defeats async benefits
- [ ] Mentions `run_in_executor` for blocking operations
- [ ] Understands that `async def` adds overhead
- [ ] Can give example where `async def` hurts performance (CPU-bound)

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Q2: FastAPI Advanced Patterns

- [ ] Explains FastAPI dependency injection system
- [ ] Understands dependencies with `yield` (setup/teardown)
- [ ] Provides good example (database connections, file handles)
- [ ] Explains difference between `BackgroundTasks` and Celery
- [ ] Explains `asyncio.create_task()` use case
- [ ] Understands trade-offs between different approaches
- [ ] Explains database connection pooling
- [ ] Mentions common pitfalls (connection leaks, pool exhaustion)

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Q3: Error Handling & Middleware

- [ ] Explains how to implement global exception handling
- [ ] Understands difference between exception handlers and middleware
- [ ] Can explain middleware execution flow
- [ ] Can describe creating timing middleware
- [ ] Explains database transaction rollback handling
- [ ] Understands async context managers for transactions
- [ ] Mentions proper cleanup in exception scenarios

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

## Part 2: Background Tasks & Workers (10 minutes)

### Q4: Background Tasks Architecture

- [ ] Explains when to use `BackgroundTasks` vs Celery
- [ ] Understands trade-offs (simplicity vs reliability)
- [ ] Explains difference between task queues and message brokers
- [ ] Understands how they work together
- [ ] Explains what happens on application crash/restart
- [ ] Mentions persistence and reliability strategies

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Q5: Celery & Distributed Workers

- [ ] Explains Celery task routing
- [ ] Understands direct exchange (exact match)
- [ ] Understands topic exchange (pattern matching)
- [ ] Understands fanout exchange (broadcast)
- [ ] Explains task priorities (0-9 scale)
- [ ] Can describe implementing priority queue
- [ ] Explains retry strategies
- [ ] Understands `autoretry_for` vs manual retry
- [ ] Explains exponential backoff
- [ ] Explains result backend concept
- [ ] Understands Redis vs RabbitMQ vs database trade-offs

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Q6: Job Processing Patterns

- [ ] Explains `task.delay()` vs `task.apply_async()`
- [ ] Understands when to use each
- [ ] Explains Celery Beat for periodic tasks
- [ ] Can describe implementing scheduler
- [ ] Explains handling long-running tasks
- [ ] Mentions `task_time_limit`, `task_acks_late`
- [ ] Explains task chaining (sequential)
- [ ] Explains task grouping (parallel)
- [ ] Explains callbacks
- [ ] Provides practical use cases

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

## Part 3: System Design & Best Practices (10 minutes)

### Q7: Scalability & Performance

- [ ] Describes approach to handle 10K concurrent requests
- [ ] Mentions connection pooling
- [ ] Mentions load balancing
- [ ] Identifies bottlenecks (database, I/O, CPU)
- [ ] Explains preventing memory leaks
- [ ] Mentions common sources (unclosed connections, circular refs)
- [ ] Explains rate limiting implementation
- [ ] Understands in-memory vs distributed rate limiting
- [ ] Mentions token bucket or sliding window algorithms

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Q8: Database & ORM Patterns

- [ ] Explains database migration approach (Alembic)
- [ ] Describes schema change management strategy
- [ ] Explains N+1 query problem
- [ ] Understands solutions (eager loading, `joinedload`, `selectinload`)
- [ ] Explains connection retry logic
- [ ] Mentions exponential backoff for retries
- [ ] Explains circuit breaker pattern
- [ ] Understands when to use circuit breakers

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Q9: Testing & Debugging

- [ ] Explains testing async FastAPI endpoints
- [ ] Mentions `TestClient` from `fastapi.testing`
- [ ] Mentions `pytest-asyncio`
- [ ] Understands challenges with async testing
- [ ] Explains testing background tasks/Celery
- [ ] Mentions mocking strategies
- [ ] Mentions `CELERY_TASK_ALWAYS_EAGER` for testing
- [ ] Explains debugging distributed systems
- [ ] Mentions logging strategies (structured logging, correlation IDs)
- [ ] Mentions monitoring tools (Prometheus, Grafana)

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

### Q10: Production Considerations

- [ ] Explains graceful shutdown handling
- [ ] Mentions SIGTERM handling, waiting for tasks
- [ ] Describes monitoring and alerting strategy
- [ ] Mentions metrics (success/failure rates, execution times)
- [ ] Explains task deduplication approach
- [ ] Mentions task IDs, Redis locks, idempotency keys
- [ ] Explains task result caching
- [ ] Understands when caching is appropriate
- [ ] Mentions TTL and cache invalidation

**Notes:**
```
_______________________________________________________
_______________________________________________________
_______________________________________________________
```

---

## Overall Assessment

### Technical Depth
- [ ] Excellent (4/4) - Deep understanding, can explain nuances
- [ ] Good (3/4) - Solid understanding, minor gaps
- [ ] Satisfactory (2/4) - Basic understanding, needs guidance
- [ ] Needs Improvement (1/4) - Surface level, struggles with concepts

### Architecture Knowledge
- [ ] Excellent (4/4) - Can choose appropriate patterns, explains trade-offs
- [ ] Good (3/4) - Understands most patterns, some gaps
- [ ] Satisfactory (2/4) - Basic pattern knowledge
- [ ] Needs Improvement (1/4) - Limited understanding

### Problem-Solving
- [ ] Excellent (4/4) - Practical solutions, considers edge cases
- [ ] Good (3/4) - Good solutions, some gaps
- [ ] Satisfactory (2/4) - Basic problem-solving
- [ ] Needs Improvement (1/4) - Struggles with complex problems

### Best Practices
- [ ] Excellent (4/4) - Strong production experience, knows best practices
- [ ] Good (3/4) - Good knowledge, some production experience
- [ ] Satisfactory (2/4) - Basic knowledge
- [ ] Needs Improvement (1/4) - Limited knowledge

### Communication
- [ ] Excellent (4/4) - Clear, articulate, explains complex concepts well
- [ ] Good (3/4) - Generally clear, minor communication issues
- [ ] Satisfactory (2/4) - Basic communication, sometimes unclear
- [ ] Needs Improvement (1/4) - Struggles to explain concepts

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

**Real-World Experience Indicators:**
- [ ] Provides concrete examples from past projects
- [ ] Discusses challenges faced and solutions
- [ ] Shows understanding of production concerns
- [ ] Mentions specific tools/technologies used

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

