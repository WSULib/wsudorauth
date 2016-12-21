# WSUDORauth
WSUDORauth is a small, Django app for authenticating users for the WSUDOR infrastructure.  It uses LDAP bindings for python and Django, and once users are logged in, stores sessions in SQL that can be referenced and utilized by other applications.  

And that's about it!  The goal was to keep WSUDORauth small and simple.  While it does have front-facing login pages, and the default Django admin capabilities, it also has some JSON-based, API-like routes that can be used for checking users and sessions that may be logged in.

WSUDORauth uses a browser cookie named `WSUDOR` to note your session ID.

## API routes

Note: when [deployed in Apache](https://github.com/WSULib/fedora-stack/blob/v2/install_scripts/wsudorauth.sh) via our [Fedora-Stack system build](https://github.com/WSULib/fedora-stack/tree/v2)

`/login?next=[URL]`
  * WSUDOR login screen
  * option `next` parameter that redirects after successful login

`/logout`
  * faceless route that logouts, and redirects to `/login`
  
`/whoami`
  * returns information about currently logged in user, via `WSUDOR` browser cookie
  * sample response<br>
  ```
  {
      username: "foobar",
      first_name: "Foo",
      last_name: "Bar",
      session_check: "http://192.168.42.6/wsudorauth/session_check/qwertyuiopasdfghkj",
      session_id: "qwertyuiopasdfghkj"
  }
  ```