import requests

class APIHelper(object):

    def api_response(self, method, url, payload={}, query={}, auth_token=None):
        '''
        Get Json response for the given api
        :param method: HTTP Method "GET", "POST", "PUT", "DELETE"
        :param url: URL of the API End point
        :param payload: payload dict for the POST method {}
        :param query: {}
        :param auth_token: Auth Token to be included in the header
        :return:
        '''
        headers = {'Content-Type': "application/json"}

        if auth_token:
            headers['Authorization'] = auth_token

        response = requests.request(method=method, url=url, headers=headers, params=query, data=payload)
        return response

    def get_api_response(self, method='GET', url=None, payload={}, query={}, auth_token=None):
        '''
        Get Json response for the given api
        :param method: HTTP Method "GET"
        :param url: URL of the API End point
        :param payload: payload dict for the POST method {}
        :param query: {}
        :param auth_token: Auth Token to be included in the header
        :return:
        '''

        headers = {'Content-Type': "application/json"}

        if auth_token:
            headers['Authorization'] = auth_token

        return self.api_response(method=method, url=url, headers=headers, params=query, data=payload)

    def post_api_response(self, method='POST', url=None, payload={}, query={}, auth_token=None):
        '''
        Get Json response for the given api
        :param method: HTTP Method : "POST"
        :param url: URL of the API End point
        :param payload: payload dict for the POST method {}
        :param query: {}
        :param auth_token: Auth Token to be included in the header
        :return:
        '''

        headers = {'Content-Type': "application/json"}

        if auth_token:
            headers['Authorization'] = auth_token

        return self.api_response(method=method, url=url, headers=headers, params=query, data=payload)

    def put_api_response(self, method='PUT', url=None, payload={}, query={}, auth_token=None):
        '''
        Get Json response for the given api
        :param method: HTTP Method : "PUT"
        :param url: URL of the API End point
        :param payload: payload dict for the POST method {}
        :param query: {}
        :param auth_token: Auth Token to be included in the header
        :return:
        '''

        headers = {'Content-Type': "application/json"}

        if auth_token:
            headers['Authorization'] = auth_token

        return self.api_response(method=method, url=url, headers=headers, params=query, data=payload)

    def delete_api_response(self, method='DELETE', url=None, payload={}, query={}, auth_token=None):
        '''
        Get Json response for the given api
        :param method: HTTP Method : "DELETE"
        :param url: URL of the API End point
        :param payload: payload dict for the POST method {}
        :param query: {}
        :param auth_token: Auth Token to be included in the header
        :return:
        '''

        headers = {'Content-Type': "application/json"}

        if auth_token:
            headers['Authorization'] = auth_token

        return self.api_response(method=method, url=url, headers=headers, params=query, data=payload)