from typing import Dict,Tuple, List
from sqlite3 import Connection

class ActivitiesRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_activity(self,activit_infos: Dict) ->None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO activits
                    (id, trip_id, title, occurs_at)
                VALUES
                    (?, ?, ?)
            """,(
                activit_infos['id'],
                activit_infos['trip_id'],
                activit_infos['title'],
                activit_infos['occurs_at'],
            )
        )

        self.__conn.commit()
        
    def find__activities_from_trip(self,trip_id:str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
        """
        SELECT * FROM activits WHERE trip_id = ?    
        """,(trip_id,)
        )

        activits = cursor.fetchall()
        return activits
    
