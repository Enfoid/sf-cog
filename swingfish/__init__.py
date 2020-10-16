from swingfish.swingfish import SwingFish


def setup(bot):
    bot.remove_command("urban")
    bot.remove_command("help")
    bot.remove_command("info")
    bot.remove_command("userinfo")
    bot.remove_command("serverinfo")
    bot.add_cog(SwingFish(bot))