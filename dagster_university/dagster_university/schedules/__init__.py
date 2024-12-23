from dagster import ScheduleDefinition
from ..jobs import trip_update_job, trips_by_week_job

trip_update_schedule = ScheduleDefinition(
    job=trip_update_job,
    cron_schedule="0 0 5 * *", # every 5th of the month at midnight
)

trips_by_week_schedule = ScheduleDefinition(
    job=trips_by_week_job,
    cron_schedule="0 0 * * 1"  # Monday at midnight
)