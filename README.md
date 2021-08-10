# A [Simple JWT](https://github.com/jazzband/djangorestframework-simplejwt) Demo.

> Simple JWT is a JSON Web Token authentication plugin for the Django REST Framework.

Reference:
- https://django-rest-framework-simplejwt.readthedocs.io/
- https://www.jetbrains.com/pycharm/guide/tutorials/django-aws/rest-api-jwt/
    - https://github.com/mukulmantosh/SampleDemo
- https://www.youtube.com/watch?v=Fhcn2qx-4VQ


# Cookie Session vs. Json Web Token

- Introduction to JSON Web Tokens:
  https://jwt.io/introduction
- JWT authentication: Best practices and when to use it:
  https://blog.logrocket.com/jwt-authentication-best-practices/

[![Session](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgRnJvbnQgRW5kXG4gICAgcGFydGljaXBhbnQgQmFjayBFbmRcbiAgICBGcm9udCBFbmQtPj5CYWNrIEVuZDogTG9naW4gUmVxdWVzdFxuICAgIE5vdGUgcmlnaHQgb2YgQmFjayBFbmQ6IFN0b3JlIFNlc3Npb25JRCBhbmQgaXRzIHZhbHVlIGluIFNlc3Npb25cbiAgICBCYWNrIEVuZC0-PkZyb250IEVuZDogUmVzcG9uc2UgYnJpbmcgU2Vzc2lvbklEXG4gICAgTm90ZSBsZWZ0IG9mIEZyb250IEVuZDogU3RvcmUgU2Vzc2lvbklEIEluIENvb2tpZVxuICAgIEZyb250IEVuZC0tPkJhY2sgRW5kOiBUaGUgUmVxdWVzdCBBZnRlciBMb2dpblxuICAgIEZyb250IEVuZC0-PkJhY2sgRW5kOiBUaGUgUmVxdWVzdCBCcmluZyBUb2tlblxuICAgIE5vdGUgcmlnaHQgb2YgQmFjayBFbmQ6IFZlcmlmeSB0aGF0IHRoZSBTZXNzaW9uSUQncyB2YWx1ZSBpcyB2YWxpZFxuICAgIEJhY2sgRW5kLT4-RnJvbnQgRW5kOiBSZXNwb25zZVxuICAgIEZyb250IEVuZC0-PkJhY2sgRW5kOiBTaWduIE91dCBvciBEZWxldGUgQWNjb3VudFxuICAgIE5vdGUgcmlnaHQgb2YgQmFjayBFbmQ6IFJlbW92ZSBTZXNzaW9uSUQgZnJvbSBTZXNzaW9uXG4gICAgQmFjayBFbmQtPj5Gcm9udCBFbmQ6IFJlc3BvbnNlXG4gICAgTm90ZSBsZWZ0IG9mIEZyb250IEVuZDogUmVtb3ZlIFNlc3Npb25JRCBmcm9tIGNvb2tpZSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgRnJvbnQgRW5kXG4gICAgcGFydGljaXBhbnQgQmFjayBFbmRcbiAgICBGcm9udCBFbmQtPj5CYWNrIEVuZDogTG9naW4gUmVxdWVzdFxuICAgIE5vdGUgcmlnaHQgb2YgQmFjayBFbmQ6IEdlbmVyYXRlIEp3dCBUb2tlblxuICAgIEJhY2sgRW5kLT4-RnJvbnQgRW5kOiBSZXNwb25zZVxuICAgIE5vdGUgbGVmdCBvZiBGcm9udCBFbmQ6IFN0b3JlIEp3dCBUb2tlbiBJbiBMb2NhbFN0b3JhZ2VcbiAgICBGcm9udCBFbmQtLT5CYWNrIEVuZDogVGhlIFJlcXVlc3QgQWZ0ZXIgTG9naW5cbiAgICBGcm9udCBFbmQtPj5CYWNrIEVuZDogVGhlIFJlcXVlc3QgQnJpbmcgVG9rZW4gPGJyLz4gSW4gSGVhZGVyJ3MgQXV0aFxuICAgIE5vdGUgcmlnaHQgb2YgQmFjayBFbmQ6IFZlcmlmeSB0aGF0IHRoZSB0b2tlbiBpcyB2YWxpZFxuICAgIEJhY2sgRW5kLT4-RnJvbnQgRW5kOiBSZXNwb25zZVxuICAgIEZyb250IEVuZC0-PkJhY2sgRW5kOiBTaWduIE91dCBvciBEZWxldGUgQWNjb3VudFxuICAgIE5vdGUgcmlnaHQgb2YgQmFjayBFbmQ6IEFkZCB0aGUgdG9rZW4gdG8gYmxhY2tsaXN0XG4gICAgQmFjayBFbmQtPj5Gcm9udCBFbmQ6IFJlc3BvbnNlXG4gICAgTm90ZSBsZWZ0IG9mIEZyb250IEVuZDogUmVtb3ZlIHRva2VuIGZyb20gbG9jYWxTdG9yYWdlIiwibWVybWFpZCI6IntcbiAgXCJ0aGVtZVwiOiBcImRlZmF1bHRcIlxufSIsInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)

[![JWT](https://mermaid.ink/img/eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgRnJvbnQgRW5kXG4gICAgcGFydGljaXBhbnQgQmFjayBFbmRcbiAgICBGcm9udCBFbmQtPj5CYWNrIEVuZDogTG9naW4gUmVxdWVzdFxuICAgIE5vdGUgcmlnaHQgb2YgQmFjayBFbmQ6IEdlbmVyYXRlIEpzb24gV2ViIFRva2VuXG4gICAgQmFjayBFbmQtPj5Gcm9udCBFbmQ6IFJlc3BvbnNlXG4gICAgTm90ZSBsZWZ0IG9mIEZyb250IEVuZDogU3RvcmUgVG9rZW4gSW4gTG9jYWxTdG9yYWdlXG4gICAgRnJvbnQgRW5kLS0-QmFjayBFbmQ6IFRoZSBSZXF1ZXN0IEFmdGVyIExvZ2luXG4gICAgRnJvbnQgRW5kLT4-QmFjayBFbmQ6IFRoZSBSZXF1ZXN0IEJyaW5nIFRva2VuIDxici8-IEluIEhlYWRlcidzIEF1dGhcbiAgICBOb3RlIHJpZ2h0IG9mIEJhY2sgRW5kOiBWZXJpZnkgdGhhdCB0aGUgVG9rZW4gaXMgdmFsaWRcbiAgICBCYWNrIEVuZC0-PkZyb250IEVuZDogUmVzcG9uc2VcbiAgICBGcm9udCBFbmQtPj5CYWNrIEVuZDogU2lnbiBPdXQgb3IgRGVsZXRlIEFjY291bnRcbiAgICBOb3RlIHJpZ2h0IG9mIEJhY2sgRW5kOiBBZGQgdGhlIFRva2VuIHRvIGJsYWNrbGlzdFxuICAgIEJhY2sgRW5kLT4-RnJvbnQgRW5kOiBSZXNwb25zZVxuICAgIE5vdGUgbGVmdCBvZiBGcm9udCBFbmQ6IFJlbW92ZSBUb2tlbiBmcm9tIExvY2FsU3RvcmFnZSIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/edit/##eyJjb2RlIjoic2VxdWVuY2VEaWFncmFtXG4gICAgcGFydGljaXBhbnQgRnJvbnQgRW5kXG4gICAgcGFydGljaXBhbnQgQmFjayBFbmRcbiAgICBGcm9udCBFbmQtPj5CYWNrIEVuZDogTG9naW4gUmVxdWVzdFxuICAgIE5vdGUgcmlnaHQgb2YgQmFjayBFbmQ6IEdlbmVyYXRlIEpzb24gV2ViIFRva2VuXG4gICAgQmFjayBFbmQtPj5Gcm9udCBFbmQ6IFJlc3BvbnNlXG4gICAgTm90ZSBsZWZ0IG9mIEZyb250IEVuZDogU3RvcmUgVG9rZW4gSW4gTG9jYWxTdG9yYWdlXG4gICAgRnJvbnQgRW5kLS0-QmFjayBFbmQ6IFRoZSBSZXF1ZXN0IEFmdGVyIExvZ2luXG4gICAgRnJvbnQgRW5kLT4-QmFjayBFbmQ6IFRoZSBSZXF1ZXN0IEJyaW5nIFRva2VuIDxici8-IEluIEhlYWRlcidzIEF1dGhcbiAgICBOb3RlIHJpZ2h0IG9mIEJhY2sgRW5kOiBWZXJpZnkgdGhhdCB0aGUgVG9rZW4gaXMgdmFsaWRcbiAgICBCYWNrIEVuZC0-PkZyb250IEVuZDogUmVzcG9uc2VcbiAgICBGcm9udCBFbmQtPj5CYWNrIEVuZDogU2lnbiBPdXQgb3IgRGVsZXRlIEFjY291bnRcbiAgICBOb3RlIHJpZ2h0IG9mIEJhY2sgRW5kOiBBZGQgdGhlIFRva2VuIHRvIGJsYWNrbGlzdFxuICAgIEJhY2sgRW5kLT4-RnJvbnQgRW5kOiBSZXNwb25zZVxuICAgIE5vdGUgbGVmdCBvZiBGcm9udCBFbmQ6IFJlbW92ZSBUb2tlbiBmcm9tIG9jYWxTdG9yYWdlIiwibWVybWFpZCI6IntcbiAgXCJ0aGVtZVwiOiBcImRlZmF1bHRcIlxufSIsInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)

# 