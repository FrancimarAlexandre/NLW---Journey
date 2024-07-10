from typing import Dict, List, Tuple
from sqlite3 import Connection

class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn
    
    def generat_link(self,links_info: Dict):
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
            INSERT INTO links
            VALUES
              (?,?,?,?)
            ''',(
                links_info['id'],
                links_info['trip_id'],
                links_info['link'],
                links_info['title'],
            )
        )
        self.__conn.commit()

    def find__links_from_trip(self,trip_id:str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
        """
        SELECT * FROM links WHERE trip_id = ?    
        """,(trip_id,)
        )

        trip = cursor.fetchall()
        return trip
