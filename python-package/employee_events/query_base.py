# Import any dependencies needed to execute sql queries
# YOUR CODE HERE
from .sql_execution import QueryMixin

# Define a class called QueryBase
# Use inheritance to add methods
# for querying the employee_events database.
# YOUR CODE HERE
class QueryBase(QueryMixin):
    pass

    # Create a class attribute called `name`
    # set the attribute to an empty string
    # YOUR CODE HERE
    name = ""
    id_check = ""
    # Define a `names` method that receives
    # no passed arguments
    # YOUR CODE HERE
    def names(self):
        return self.query(f"SELECT first_name, last_name FROM {self.name}")

        # Return an empty list
        # YOUR CODE HERE
    def empty_method(self):  # ← what is this method called?
        return []

    # Define an `event_counts` method
    # that receives an `id` argument
    # This method should return a pandas dataframe
    # YOUR CODE HERE

    def event_counts(self, id):
        return self.pandas_query(f"SELECT positive_events, negative_events FROM employee_events WHERE {self.id_check} = {id}")

        # QUERY 1
        # Write an SQL query that groups by `event_date`
        # and sums the number of positive and negative events
        # Use f-string formatting to set the FROM {table}
        # to the `name` class attribute
        # Use f-string formatting to set the name
        # of id columns used for joining
        # order by the event_date column
        # YOUR CODE HERE
            
    def event_date(self, id):
        return self.pandas_query(f"SELECT event_date, SUM(positive_events), SUM(negative_events) FROM employee_events WHERE {self.id_check} = {id} GROUP BY event_date ORDER BY event_date")

    # Define a `notes` method that receives an id argument
    # This function should return a pandas dataframe
    # YOUR CODE HERE
    def notes(self, id):
        return self.pandas_query(f"SELECT note_date, note FROM notes JOIN {self.name} ON notes.{self.id_check} = {self.name}.{self.id_check} WHERE notes.{self.id_check} = {id}")


        # QUERY 2
        # Write an SQL query that returns `note_date`, and `note`
        # from the `notes` table
        # Set the joined table names and id columns
        # with f-string formatting
        # so the query returns the notes
        # for the table name in the `name` class attribute
        # YOUR CODE HERE

