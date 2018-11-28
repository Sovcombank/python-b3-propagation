from requests.sessions import Session

from b3_propagation import get_zipkin_headers


class ZipkinHeadersSession(Session):
    def request(self, method, url, **kwargs):
        zipkin_headers = get_zipkin_headers()
        updated_kwargs = dict(kwargs)
        updated_kwargs['headers'] = kwargs.get('headers', {}).copy()
        updated_kwargs['headers'].update(zipkin_headers)
        return super(ZipkinHeadersSession, self).request(method, url, **updated_kwargs)
