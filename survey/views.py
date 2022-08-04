import cloudinary.uploader
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

# =============================================================================
# CONSTANT VARIABLES
all_answers = []
rana_acc = 'ranaz.omarz@gmail.com'
rawan_acc = 'rawaneldalie@gmail.com'


# =============================================================================

def uploadImage():
    # Upload the image and get its URL
    # ==============================

    # Upload the image.
    # Set the asset's public ID and allow overwriting the asset with new versions
    cloudinary.uploader.upload("https://cloudinary-devs.github.io/cld-docs-assets/assets/images/butterfly.jpeg",
                               public_id="quickstart_butterfly", unique_filename=False, overwrite=True)

    # Build the URL for the image and save it in the variable 'srcURL'
    srcURL = cloudinary.CloudinaryImage("quickstart_butterfly").build_url()

    # Log the image URL to the console.
    # Copy this URL in a browser tab to generate the image on the fly.
    print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")
uploadImage()


# =============================================================================
# SEND EMAIL FUNCTION
# =============================================================================
def send_email(msg, name, email, phone):
    import smtplib

    # SET EMAIL LOGIN REQUIREMENTS
    gmail_user = 'kadellform@gmail.com'
    gmail_app_password = 'zuajtmownuovcliw'

    # SET THE INFO ABOUT THE SAID EMAIL
    sent_from = gmail_user
    sent_to = [rana_acc, rawan_acc]
    sent_subject = "New Form"
    sent_body = f"{str(msg).encode('UTF-8')}\n\n" \
                f"Name: {name}\n" \
                f"Email: {email}\n" \
                f"Phone Number: {phone}"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

    # SEND EMAIL OR DIE TRYING!!!
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text)
        server.close()

        print('Email sent!')
    except Exception as exception:
        print("Error: %s!\n\n" % exception)


# =============================================================================
# SURVEY FORM ROUTE
# =============================================================================
def survey(request):
    global all_answers

    # TRY TO GET ALL_ANSWERS
    try:
        all_answers = [request.GET['q1'], request.GET['q2'], request.GET['q3'], request.GET['q4'], request.GET['q5'],
                       request.GET['q6'], request.GET['q7'], request.GET['q8'], request.GET['q9'], request.GET['q10'],
                       request.GET['q11']]

        return render(request, 'submit.html')

    except MultiValueDictKeyError:
        pass

    return render(request, 'survey.html')


# =============================================================================
# SUBMIT NAME, EMAIL ANS NUMBER FORM ROUTE
# =============================================================================
def submit(request):
    # TRY TO GET NAME, EMAIL AND PHONE_NUMBER
    try:
        name = request.GET['name']
        email = request.GET['email']
        phone_number = request.GET['phone_number']

        # FORMATTING THE MESSAGE
        msg = ""
        for answer in all_answers:
            msg += f" ({answer}) "

        # SENDING THE TEST ANSWERS
        send_email(msg, name, email, phone_number)

        return render(request, 'done.html')

    except MultiValueDictKeyError:
        pass

    return render(request, 'submit.html')


def done(request):
    return render(request, 'done.html')
