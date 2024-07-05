class ResponseSuccess:
    response_registered = {"message": "You have successfully registered"}
    response_already_registered = {"message": "You are already registered"}
    response_logged_in = {"message": "You are successfully logged in"}
    response_already_logged_in = {"message": "You are already logged in"}


class ResponseFailure:
    response_not_logged_in = {"message": "You are not logged in"}
    response_incorrect_data = {"message": "Either your email or your password are incorrect. Please try again"}
    response_not_registered = {"message": "You are not registered. Please try again later"}
