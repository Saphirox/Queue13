# Queues performance producer 30 seconds

| Queue     | Concurrency | Availability % | Success |
|-----------|-------------|----------------|---------|
| Beanstalk | 20          | 100            | TRUE    |
| Beanstalk | 50          | 100            | TRUE    |
| Beanstalk | 100         | 93             | FALSE   |
| RDB       | 20          | 100            | TRUE    |
| RDB       | 50          | 94             | FALSE   |
| RDB       | 100         | 94             | FALSE   |
| AOF       | 94          | 94             | FALSE   |
| AOF       | 50          | 94             | FALSE   |
| AOF       | 100         | 94             | FALSE   |
