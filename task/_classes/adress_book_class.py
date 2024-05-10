from _classes.records_class import Record
from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        name = name.lower()
        for _, record in self.data.items():
            if record.name.value.lower() == name:
                return record
        raise ValueError("Record not found.")
    
    def delete(self, name):
        for key, record in self.data.items():
            if record.name.value.lower() == name.lower():  
                del self.data[key]  
                print(f"Record for {name} deleted") 
                return 
        raise ValueError("Record not found.")