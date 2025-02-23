
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
from flask import Flask,jsonify


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
    "id": self._generateId,
    "first_name": "John Jackson",
    "age": 33,
    "lucky_numbers": [7, 13, 22]
}
{
    "id": self._generateId,
    "first_name": "Jane Jackson",
    "age": 35,
    "lucky_numbers": [10, 14, 3]
}
{
    "id": self._generateId,
    "first_name": "Jimmy Jackson",
    "age": 5,
    "lucky_numbers": [1]
}]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
    

    def add_member(self, member):
        # fill this method and update the return
        json_text = self._members.append(member)
        print (f"Se agrego el miembro: {member}")
        return json_text(self._members)


    def delete_member(self, id):        
        del self._members[id];
        print(f"Se elimino el miembro: {id}")
        return jsonify(self._members)


    def get_member(self, id):
        json_text = self.members[id];
        for i in range (len(self._members)):
            if self._members[i].get("id") == id
                return self._members[i];
        print{f"El miembro es: {json_text}"}
        return jsonify(json_text)


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
