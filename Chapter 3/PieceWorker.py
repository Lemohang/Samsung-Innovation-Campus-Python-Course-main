from Employee import Employee
class Pieceworker(Employee):
    def __init__(self, id, name, dept_id, address, no_of_pieces_produced, rate_per_piece):
        super().__init__(id, name, dept_id, address)
        self.no_of_pieces_produced = no_of_pieces_produced
        self.rate_per_piece = rate_per_piece

    def set_no_of_pieces_produced(self, no_of_pieces_produced):
        self.no_of_pieces_produced = no_of_pieces_produced

    def set_rate_per_piece(self, rate_per_piece):
        self.rate_per_piece = rate_per_piece

    def get_no_of_pieces_produced(self):
        return self.no_of_pieces_produced

    def get_rate_per_piece(self):
        return self.rate_per_piece

    def calculate_salary(self):
        return self.no_of_pieces_produced * self.rate_per_piece
def __str__(self):
    return "{},Piece Worker: {}, ID: {}, Salary: {:.2f}, Department: {}".format(super().__str__(),
        self.name, self.id, self.calculate_salary(), self.department
    )
