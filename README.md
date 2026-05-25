users = []
resources = []
violations = []


class DataStorage:
    def get_all_users(self):
        return users

    def get_user_by_username(self, username):
        for u in users:
            if u.get("username") == username:
                return u
        return None

    def get_user_by_id(self, user_id):
        for u in users:
            if u.get("id") == user_id:
                return u
        return None

    def add_user(self, user):
        users.append(user)

    def get_all_resources(self):
        return resources

    def add_resource(self, resource):
        resources.append(resource)

    def delete_resource(self, resource_id):
        global resources
        resources[:] = [r for r in resources if r.get("id") != resource_id]

    def get_all_violations(self):
        return violations

    def add_violation(self, violation):
        violations.append(violation)
