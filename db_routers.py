class UserBookRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'user_db'
        elif model._meta.app_label == 'books':
            return 'book_db'
            # default for others
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'user_db'
        elif model._meta.app_label == 'books':
            return 'book_db'
            # default for others
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        db_list = ('user_db', 'book_db', 'default')
        if (obj1._state.db in db_list) and (obj2._state.db in db_list):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'users':
            return db == 'user_db'
        elif app_label == 'books':
            return db == 'book_db'
        # others on default DB
        return db == 'default'
