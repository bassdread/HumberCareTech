from flask import Flask, render_template

# EB looks for an 'application' callable by default.
application = Flask(__name__)


CARE_PLAN_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
          integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

</head>

<body>
<main role="main">

    <!-- Example row of columns -->
    <div class="row">
        <div class="col-md-12">
            <h2>05/09/2018</h2>
            <div class="list-group">
                <a href="#" class="list-group-item list-group-item-action">Assist with getting in/out of bed</a>
                <a href="#" class="list-group-item list-group-item-action">Make Bed</a>
                <a href="#" class="list-group-item list-group-item-action">Change Bed Linen</a>
                <a href="#" class="list-group-item list-group-item-action">Help with bathing</a>
                <a href="#" class="list-group-item list-group-item-action">Help with toileting</a>
                <a href="#" class="list-group-item list-group-item-action">Help with grooming</a>
                <a href="#" class="list-group-item list-group-item-action">Help with dressing</a>
                <a href="#" class="list-group-item list-group-item-action">Manage Medication</a>
                <a href="#" class="list-group-item list-group-item-action">Prepare and serve meals</a>
            </div>
            <h2>Advice from Guardian</h2>
            <div class="list-group">
                <a href="#" class="list-group-item 
                list-group-item-action">Ensure the bins are taken out</a>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            <h2>Last Updated: 02/09/2018 - 09:45:00</h2>
        </div>
    </div>
    
    <a class="btn btn-success" href="/success" role="Success">Success</a>
</main>

<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
        integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
        integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
        crossorigin="anonymous"></script>
</body>
</html>
'''


LOGIN = '''

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Login</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<link rel="stylesheet" href="http://getbootstrap.com/docs/4.1/examples/sign-in/signin.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">


    <!-- Custom styles for this template -->
    <link href="signin.css" rel="stylesheet">
  </head>

  <body class="text-center">
    <form class="form-signin">
      <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
      <label for="inputEmail" class="sr-only">Email address</label>
      <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
      <label for="inputPassword" class="sr-only">Password</label>
      <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>
      <div class="checkbox mb-3">
        <label>
          <input type="checkbox" value="remember-me"> Remember me
        </label>
      </div>
      <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
      <p class="mt-5 mb-3 text-muted">&copy; 2017-2018</p>
    </form>
  </body>
</html>
'''


SUCCESS = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Completed</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <link rel="stylesheet" href="http://getbootstrap.com/docs/4.1/examples/sign-in/signin.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

  </head>

  <body class="text-center">
    <h1>Completed</h1>
  </body>
</html>
'''


HELP = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Support</title>

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <link rel="stylesheet" href="http://getbootstrap.com/docs/4.1/examples/sign-in/signin.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

  </head>

  <body class="text-center">
<main role="main">

      <!-- Main jumbotron for a primary marketing message or call to action -->
      <div class="jumbotron">
        <div class="container">
          <h1 class="display-3">Support</h1>
          <p>Support and help for using the CareHub services.</p>
        </div>
      </div>

      <div class="container">
        <!-- Example row of columns -->
        <div class="row">
          <div class="col-md-12">
            <h1>Setup</h1>
            <p>The service user (care receiver) will receive a postcard 
            either in the post or delivered on the first visit. The career 
            will use this postcard to register their visit and receive a 
            detailed care plan from our hub.</p>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <h1>Subscription</h1>
            <p>A recurring subscription model, billed on a monthly cycle.</p>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <h1>Guardians</h1>
            <p>Our service gives you peace that your loved is receiving the 
            care you expect.</p>
            <p>Each visit is logged and updates are uploaded to our Hub for 
            you to view.</p>
          </div>
        </div>
        <hr>
      </div> <!-- /container -->

    </main>
  </body>
</html>
'''



GUARDIAN = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
          integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

</head>

<body>

    <main role="main">

      <div class="container">
        <!-- Example row of columns -->
        <div class="row">
          <div class="col-md-12">
            <h2>Visits</h2>
            <table class="table">
              <thead>
                <tr>
                  <th scope="col">Carer</th>
                  <th scope="col">Logged In</th>
                  <th scope="col">Logged Out</th>
                  <th scope="col">Comments</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>Dawn</td>
                  <td>01/09/2018 - 10:15:00</td>
                  <td>01/09/2018 - 11:15:00</td>
                  <td>They were feeling down</td>
                </tr>
              </tbody>
              <tbody>
                <tr>
                  <td>David</td>
                  <td>01/09/2018 - 10:00:00</td>
                  <td>01/09/2018 - 10:45:00</td>
                  <td>Put bins out</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <h2>Last Updated: 02/09/2018 - 12:45:00</h2>
            </div>
        </div>
        <hr>

      </div> <!-- /container -->
    
</main>

<!-- Bootstrap core JavaScript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
        integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
        crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
        integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
        crossorigin="anonymous"></script>
</body>
</html>
'''


@application.route('/login')
def login():
    return LOGIN


@application.route('/success')
def success():
    return SUCCESS


@application.route('/test')
def careplan():
    return CARE_PLAN_TEMPLATE


@application.route('/guardian')
def guardian():
    return GUARDIAN


@application.route('/help')
def help():
    return HELP


@application.route('/')
def index():
    return LOGIN


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
