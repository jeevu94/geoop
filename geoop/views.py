import json
import psycopg2
from django.views.generic import View
from django.http import HttpResponse


class TaskExecutor(View):

    def post(self, request, *args, **kwargs):
        database = request.POST.get("POSTGRES_DB", None)
        user = request.POST.get("POSTGRES_USER", None)
        password = request.POST.get("POSTGRES_PASSWORD", None)
        host = request.POST.get("POSTGRES_HOST", None)
        port = request.POST.get("POSTGRES_PORT", None)
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
                print('Executing PostgreSQL')
                cur.execute('SELECT count(*) FROM auth_user')

                # display the results
                res = cur.fetchall()
                response_data["result"] = res
                print(res)

                # close the communication with the PostgreSQL
                cur.close()

            except Exception as error:
                print(error)
                response_data["error"] = f"{error}"
            finally:
                if conn is not None:
                    conn.close()
                    print('Database connection closed.')

        return HttpResponse(json.dumps(response_data), content_type="application/json")
