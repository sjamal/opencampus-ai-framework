# Architecture

Architecture documentation for OpenCampus AI Framework.

                    OpenCampus AI Framework

                    +--------------------+
                    |    Web / Mobile    |
                    +---------+----------+
                              |
                        REST / HTTPS
                              |
                    +---------v----------+
                    |    FastAPI API     |
                    +---------+----------+
                              |
              +---------------+----------------+
              |               |                |
      Workflow Services   AI Services   Auth Services
              |               |                |
              +-------+-------+----------------+
                      |
               PostgreSQL / Redis
