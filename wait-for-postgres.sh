#!/bin/sh
# wait-for-postgres.sh - wait for Postgres to be ready

host="$1"
shift
cmd="$@"

until pg_isready -h "$host" -U "$DB_USER"; do
  echo "Waiting for Postgres at $host..."
  sleep 2
done

exec $cmd