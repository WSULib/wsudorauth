# WSUDORauth
WSUDORauth is a small, Django app for authenticating users for the WSUDOR infrastructure.  It uses LDAP bindings for python and Django, and once users are logged in, stores sessions in SQL that can be referenced and utilized by other applications.  

And that's about it!  The goal was to keep WSUDORauth small and simple.  While it does have front-facing login pages, and the default Django admin capabilities, it also has some JSON-based, API-like routes that can be used for checking users and sessions that may be logged in.

WSUDORauth uses a browser cookie named `WSUDOR` to note your session ID.

## API routes

Note: when [deployed in Apache](https://github.com/WSULib/fedora-stack/blob/v2/install_scripts/wsudorauth.sh) via our [Fedora-Stack system build](https://github.com/WSULib/fedora-stack/tree/v2), all routes include a `/wsudorauth` URL prefix.

`/wsudorauth/login?next=[URL]`
  * WSUDOR login screen
  * creates session and sets `WSUDOR` cookie
  * option `next` parameter that redirects after successful login

`/wsudorauth/logout`
  * faceless route that logouts, and redirects to `/login`
  
`/wsudorauth/whoami`
  * returns information about currently logged in user, via `WSUDOR` browser cookie
  * sample response:<br>
  ```
  {
      username: "foobar",
      first_name: "Foo",
      last_name: "Bar",
      session_check: "http://192.168.42.6/wsudorauth/session_check/qwertyuiopasdfghkj",
      session_id: "qwertyuiopasdfghkj"
  }
  ```
  
`/wsudorauth/session_check/[SESSION_ID]`
  * given an active, valid session id, returns the Access ID, first name, and last name of user, and `200` status code
  * given an invalid session id, returns response and `404` status code
  * no session id, `400` status code response returned
  * sample response:<br>
  ```
  {
      username: "foobar",
      first_name: "Foo",
      last_name: "Bar"
  }
  ```
