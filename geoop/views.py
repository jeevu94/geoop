import json
import psycopg2
from django.views.generic import View
from django.http import HttpResponse


class TaskExecutor(View):

    def post(self, request, *args, **kwargs):
        database = request.data.get("POSTGRES_DB", None)
        user = request.data.get("POSTGRES_USER", None)
        password = request.data.get("POSTGRES_PASSWORD", None)
        host = request.data.get("POSTGRES_HOST", None)
        port = request.data.get("POSTGRES_PORT", None)
        response_data = {}
        conn = None

        if None not in (database, user, password, host, port):
            try:
                print('Connecting to the PostgreSQL database...')
                conn = psycopg2.connect(
                    host=host,
                    database=database,
                    user=user,
                    password=password,
                    port=port,
                )

                # create a cursor
                cur = conn.cursor()

                # execute a statement
                print('PostgreSQL database version:')
                cur.execute('SELECT version()')

                # display the PostgreSQL database server version
                db_version = cur.fetchone()
                print(db_version)

                # close the communication with the PostgreSQL
                cur.close()

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()
                    print('Database connection closed.')

        return HttpResponse(json.dumps(response_data), content_type="application/json")
