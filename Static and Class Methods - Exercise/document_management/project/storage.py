class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.find_by_id(self.categories, category_id)
        if category:
            category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.find_by_id(self.topics, topic_id)
        if topic:
            topic.topic, topic.storage_folder = new_topic, new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.find_by_id(self.documents, document_id)
        if document:
            document.file_name = new_file_name

    @staticmethod
    def find_by_id(some_list, some_id):
        for value in some_list:
            if value.id == some_id:
                return value
        return False

    def delete_category(self, category_id):
        category = self.find_by_id(self.categories, category_id)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.find_by_id(self.topics, topic_id)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.find_by_id(self.documents, document_id)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        document = self.find_by_id(self.documents, document_id)
        if document:
            return document

    def __repr__(self):
        ll = []
        for document in self.documents:
            ll.append(document)

        return '\n'.join(str(x) for x in ll)