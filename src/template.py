TEMPLATES = {
    'EMAIL_SUBJECT': """
            Your Fast and Secure BeePass VPN server 🐝 🔑
        """,
    'OUTLINE_NEW_TEXT_BODY': """
            Dear User,

            Welcome to BEEPASS VPN server distribution system. By receiving this email you accepted that you opt-in to our "Distribution list". ‌For more information about privacy policy please visit our website.
            *You can unsubscribe (mailto:{DELETE_USER_EMAIL}) at anytime if you wish, but you'll lose your server!

            Click on the following button to install BEEPASS and get your personal access key to a server: {key}

            کاربر عزیز،
            به سیستم توزیع سِرور برای فیلترشکن BeePass خوش‌ آمدید. با دریافت این ایمیل، شما قبول کرده‌اید که در فهرست توزیع ما قرار بگیرید و سِرور اختصاصی دریافت کنید. برای اطلاعات بیشتر، سند حریم ‌خصوصی ما را اینجا بخوانید.
            *شما هر زمانی که بخواهید می‌توانید از طریق این آدرس {DELETE_USER_EMAIL} ایمیل خود را از لیست توزیع حذف کنید، اما در نظر داشته باشید که با این کار سِرور اختصاصی شما نیز حذف می‌شود.

            توجه: در نسل جدید سِرورهای اختصاصی، تغییرات به‌طور خودکار اعمال می‌شود و نیاز نیست که کلید جدید درخواست کنید. دریافت یک کلید از سمت شما کافی است و در صورت بروز اختلال، تیم BEEPASS تغییرات لازم را روی کلیدها اعمال می‌کند.
            با کلیک کردن بر روی دکمه زیر، فیلترشکن BEEPASS را نصب کرده و سِرور اختصاصی خود را دریافت کنید: {key}
        """,
    'NOSERVER_TEXT_BODY': """
            Dear User,

            There is no access key available at the moment.
            If you have any questions or concerns, you can contact our support channels through Telegram or Email.
            You can unsubscribe (mailto:{DELETE_USER_EMAIL}) at anytime if you wish, but you'll lose your server!

            Thank you for your patience!

            کاربر عزیز،
            متاسفانه در حال حاضر هیچ سِروری در دسترس نیست.
            اگر مشکل یا سوالی دارید، لطفا با پشتیبانی ما در تلگرام یا از طریق ایمیل تماس بگیرید.
            *شما هر زمانی که بخواهید می‌توانید از طریق این آدرس {DELETE_USER_EMAIL} ایمیل خود را از لیست توزیع حذف کنید، اما در نظر داشته باشید که با این کار سِرور اختصاصی شما نیز حذف می‌شود.

            ممنون از شکیبایی شما!
        """,
    'TRY_AGAIN_TEXT_BODY': """
            Dear User,

            Something went wrong!
            Please try again by sending an to {GET_EMAIL}
            You can unsubscribe (mailto:{DELETE_USER_EMAIL}) at anytime if you wish, but you'll lose your server!

            Thank you for your patience!

            کاربر عزیز،

            متاسفانه مشکلی پیش آمد. لطفا دوباره یک ایمیل به آدرس {GET_EMAIL} ارسال کنید.
            *شما هر زمانی که بخواهید می‌توانید از طریق این آدرس {DELETE_USER_EMAIL} ایمیل خود را از لیست توزیع حذف کنید، اما در نظر داشته باشید که با این کار سِرور اختصاصی شما نیز حذف می‌شود.

            ممنون از شکیبایی شما!
        """,
    'UNSUBSCRIBED_TEXT_BODY': """
            You unsubscribed from our mailing list, and your access key is revoked now.
            You can always subscribe back and get a new access key by just sending an email to {GET_EMAIL}


            Thank you!

            ایمیل و سِرور اختصاصی شما از فهرست توزیع ایمیلی ما حذف شد.

            شما می‌توانید با فرستادن یک ایمیل به {GET_EMAIL} دوباره به فهرست ما بپیوندید و سِرور جدید دریافت کنید.

            ممنون از شما!

        """
}
