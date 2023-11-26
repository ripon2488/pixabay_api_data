import psycopg2
from db.config import get_cursor
from psycopg2.extras import execute_values
import csv
from api.send_mail import csv_send_mail,csv_file_name


def insert_to_database(data):
    with get_cursor() as (conn,cursor):
        try:
            sql = "INSERT INTO pixa_data (page_url,tags,type,large_image_url,preview_url) VALUES %s"
            execute_values(cursor,sql,data)
            conn.commit()
            print("Data Successfully Inserted !")
            export_yn = input("Are you want to Export as .csv file? Type \"Y or N\": ")
            export_yn = export_yn.lower()
            if export_yn == "y":
                print("Exporitng your Data.....")
                # file_name = input("Enter the file name:")
                # now we will open a file for writing
                csv_fileName = csv_file_name()
                data_file = open(csv_fileName, 'w', newline ='')
                
                # create the csv writer object
                csv_writer = csv.writer(data_file)
                
                # Counter variable used for writing headers to the CSV file
                count = 0

                for d in data:
                    if count == 0:
                
                        # Writing headers of CSV file
                        header = ('page_url','tags','type','large_image_url','preview_url')
                        csv_writer.writerow(header)
                        count += 1
                
                    # Writing data of CSV file
                    csv_writer.writerow(d)
                
                data_file.close()
                print("Exported Data Successfully as .csv file !")
            else:
                print("Data Not Exported !")
            email_yn = input("Are you want to Email this csv file? Type \"Y or N\": ")
            email_yn = email_yn.lower()
            if email_yn == "y":
                csv_send_mail()
            else:
                print("Data Not Mailed !")                


        except psycopg2.DatabaseError as e:
            print("Error", e)
