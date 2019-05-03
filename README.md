# zadmin
A simple Python library to provide access to a complex Zimbra Soap interface.

## Installation
`pip install git+https://github.com/rodrigollima/zadmin.git`

### Basics
For all request you need an Auth token instance
```python
   from zadmin.auth import Auth
   
   auth = Auth('https://zimbrahost.tld:7071/service/admin/soap', 'admin@zimbrahost.tld', 'secretpassword')
   auth.token
```

### Domain
```python
   from zadmin.auth import Auth
   from zadmin.domain import Domain
   
   ## Create
   auth = Auth('https://zimbrahost.tld:7071/service/admin/soap', 'admin@zimbrahost.tld', 'secretpassword')
   domain = Domain(auth)
   d = domain.create(hostname='newhost.tld')

   ## List all
   auth = Auth('https://zimbrahost.tld:7071/service/admin/soap', 'admin@zimbrahost.tld', 'secretpassword')
   domain = Domain(auth)
   d = domain.list()

   ## Get account quantity by Class of Service
   domain = Domain(auth)
   q = domain.count_accounts_by_class_of_service('newhost.tld')
```

### Accoun creation
```python
   from zadmin.auth import Auth
   from zadmin.account import Account
   
   ## Create account
   auth = Auth('https://zimbrahost.tld:7071/service/admin/soap', 'admin@zimbrahost.tld', 'secretpassword')
   account = Account(auth)
   a = account.create(account='account@domain.tld', password='fdas@#F555AFSD',zimbraCosId='8e97e282-8aa0-4ac4-96fb-7e2e7620c0a4')

   ## Rename account
   auth = Auth('https://zimbrahost.tld:7071/service/admin/soap', 'admin@zimbrahost.tld', 'secretpassword')
   account = Account(auth)
   a = account.rename(id='bcd33ca4-ab26-48cd-ba0e-a6f68011b4bc', account='newname@domain.tld')

```

### List COS
```python
   from zadmin.auth import Auth
   from zadmin.cos import Cos
   
   auth = Auth('https://zimbrahost.tld:7071/service/admin/soap', 'admin@zimbrahost.tld', 'secretpassword')
   cos = Cos(auth)
   c = cos.list()
```

### Get Backup Query
```python
   from zadmin.auth import Auth
   from zadmin.backup import BackupQuery
   
   auth = Auth('https://zimbrahost.tld:7071/service/admin/soap', 'admin@zimbrahost.tld', 'secretpassword')
   backup = BackupQuery(auth)
   b = backup.get(account='account@zimbrahost.tld')
```

### Feature List
* `Domain`
  * creation
  * list
* `Account`
  * creation
  * rename
* `COS`
  * list
* `BackupQuery`
  * get

