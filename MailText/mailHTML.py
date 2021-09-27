def mailhtml():
    html = """\
        <html>
        <body>
            <p>Chào bạn!<br>
            Mail này được gửi tự động đến bạn.<br>        
            Hôm nay là {TODAY}.
            CHÚC BẠN MỘT NGÀY SINH NHẬT VUI VẺ
            <a href="https://github.com/OrangeFoxie/Birthday_mailer.git">Gấu mèo</a> 
            </p>
        </body>
        </html>
    """
    return html