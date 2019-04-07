import sqlite3
import json

# TODO: need a function or file to configure the path of database, and module
# TODO: can it handle types like List[str]?

table = "monkeytype_call_traces"


def return_type(function):
    """The function connects the database and make queries"""
    dbFilename = "example/monkeytype.sqlite3"
    query = "SELECT DISTINCT arg_types from " + table + " WHERE qualname == " + function
    try:
        conn = sqlite3.connect(dbFilename)
        cur = conn.cursor()
        cur.execute(query)
        row = cur.fetchone()
        if not row:
            conn.commit()
        dict_row = json.loads(row[0])  # convert the string into dictionary
        # print(dict_row.keys())  # return the parameter
        types = {}
        for k, v in dict_row.items():
            types[k] = v['qualname']
        return types  # return the parameter and its type in a dict type
    except sqlite3.Error as e:
        print("Database error: %s" % e)
    except Exception as e:  # pylint: disable=W0703
        print("Exception in _query: %s" % e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    # return_type("monkeytype_call_traces", "termfrequency")
    types_isstopwords = return_type(function="\"StopWordManager.is_stop_word\"")
    print(types_isstopwords)
    print("=================")
    types_sorted = return_type(function="\"WordFrequencyManager.sorted\"")
    print(types_sorted)