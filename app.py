from flask import Flask, request, render_template_string

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dynamic Image Share</title>
    <meta property="og:type" content="website">
    <meta property="og:url" content="{{ url_for('share_image', _external=True) }}?image={{ image_url }}">
    <meta property="og:title" content="Amazing Image">
    <meta property="og:description" content="A captivating description of the image content.">
    <meta property="og:image" content="{{ image_url }}">

    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="{{ url_for('share_image', _external=True) }}?image={{ image_url }}">
    <meta name="twitter:title" content="Amazing Image">
    <meta name="twitter:description" content="A captivating description of the image content.">
    <meta name="twitter:image" content="{{ image_url }}">
</head>
<body>
<h1>View This Image</h1>
<img src="{{ image_url }}" alt="Dynamic Image">
</body>
</html>
'''

@app.route('/share')
def share_image():
    image_url = request.args.get('image', '')
    return render_template_string(TEMPLATE, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)

