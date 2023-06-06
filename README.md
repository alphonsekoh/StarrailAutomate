# Honkai Star Rail Automation

Feel free to fork or star this repository for your reference.
It calls the HSR Daily check-in API and automates it using github actions in the main.yml from the .github directory.
You would also need to involve Github Secrets to protect your `LTOKEN` and `LTUID`, preventing bad actors from misusing your account.

### How to Set up the automation

1. Fork this repository, maybe star it as well (yes I am shameless LOL)
2. Find your `LTUID` and `LTOKEN`; instructions on the next section.
3. Head to your forked repository and add the 2 values into your repository Github Secrets. For more details on how to add them, Here's a link to guide you. [Link here](https://blog.devgenius.io/github-actions-secrets-6b8a86701703), look under the Repository Secrets paragraph.

### Finding LTUID and LTOKEN

1. To find what is your `LTUID` and `LTOKEN`, head to the daily check in site [here](https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id=e202303301540311&hyl_auth_required=true&hyl_presentation_style=fullscreen&utm_source=hoyolab&utm_medium=tools&utm_campaign=checkin&utm_id=6&lang=en-us&bbs_theme=dark&bbs_theme_device=1). Right click on your browser and click on inspect. Head to the **Network** tab, refresh the browser once and then find the results with **index.html?act_id=e202303301540311...**
2. Once clicked on the result, go under the **Cookies** tab to find your `ltoken` and `ltuid` values
