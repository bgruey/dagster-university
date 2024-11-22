# fmt: off
from dagster import Definitions, load_assets_from_modules

from .assets import metrics, requests, trips
from .jobs import adhoc_request_job, trips_by_week_job, trip_update_job
from .resources import database_resource
from .schedules import trip_update_schedule, trips_by_week_schedule
from .sensors import adhoc_request_sensor

metric_assets = load_assets_from_modules([metrics])
request_assets = load_assets_from_modules([requests])
trip_assets = load_assets_from_modules([trips])

all_jobs = [trips_by_week_job, trip_update_job, adhoc_request_job]
all_schedules = [trips_by_week_schedule, trip_update_schedule]
all_sensors = [adhoc_request_sensor]


defs = Definitions(
    assets=[*metric_assets, *request_assets, *trip_assets],
    jobs=all_jobs,
    resources={
        "database": database_resource
    },
    schedules=all_schedules,
    sensors=all_sensors,
)
