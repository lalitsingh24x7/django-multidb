class MyRouter(object):
    """
    Router class to control all database operations
    """
    def db_for_read(self, model, **hints):
        """
        Suggest the database that should be used for read operations 
        """
        return 'secondary'

    def db_for_write(self, model, **hints):
        """
        Suggest the database that should be used for writes operations
        """
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Return True if a relation between obj1 and obj2 should be allowed
        """
        db_list = ('default', 'secondary',)
        if obj1._state.db in db_list and obj2._state.db in db_list:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Return True if migration operation is allowed to run on the database
        """
        if db == 'default':
            return True
        return None