import alluka
import hikari
import tanjun
from bmo.core import chron

help = tanjun.Component(name="help")


@help.with_slash_command
@tanjun.with_str_slash_option("obj", "Object to get help for", default=False)
@tanjun.as_slash_command("help", "Shows help about all or one specific command")
async def custom_help(
    ctx: tanjun.abc.Context,
    obj: str,
    bot: alluka.Injected[hikari.GatewayBot],
) -> None:
    bot_user = bot.get_me()
    cd = chron.short_date_and_time(bot_user.created_at)

    comp_desc = ""
    for component in ctx.client.components:
        comp_desc += f"`{component}`"

    if not obj:
        embed = hikari.Embed(
            description="""Welcome to DJ BMO's help!
Find all the commands available on this panel.""",
            color=0x77F2F2,
        )
        embed.add_field(name="Modules", description=comp_desc, inline=False)
        embed.set_author(
            name="DJ BMO • Help",
            icon=bot_user.avatar_url or bot_user.default_avatar_url,
        )
        embed.set_thumbnail(bot_user.avatar_url or bot_user.default_avatar_url)
        embed.set_footer(
            text=f"DJ BMO was created {cd}",
            icon=bot_user.avatar_url or bot_user.default_avatar_url,
        )
        await ctx.respond(embed)


"""
    elif obj in ctx.client.cogs:
        plugin = ctx.client.get_cog(obj)
        await ctx.respond("this is plugin help")

    elif obj in ctx.client.all_commands:
        cmd = ctx.client.get_command(obj)
        if isinstance(cmd, commands.Group):
            await ctx.respond("this is group help")
        else:
            await ctx.respond("this is command help")
    else:
        await ctx.respond("command or category could not be found")
"""


@tanjun.as_loader
def load(client: tanjun.abc.Client) -> None:
    client.add_component(help.copy())
