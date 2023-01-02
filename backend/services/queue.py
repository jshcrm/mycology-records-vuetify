from procrastinate import AiopgConnector, App, jobs
from procrastinate.manager import JobManager

from backend.settings import Settings

settings = Settings()

connector = connector = AiopgConnector(
    host=settings.POSTGRES_HOST,
    database=settings.POSTGRES_DB,
    user=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
)

procrastinate_app = App(connector=connector)
job_manager = JobManager(connector=connector)


async def remove_job(job_id):
    await job_manager.finish_job_by_id_async(
        job_id, status=jobs.Status.FAILED, delete_job=True
    )
