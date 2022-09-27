import hikari
import tanjun

listener = tanjun.Component(name="Listeners")


@listener.with_slash_command
@tanjun.as_slash_command("foo", "Bar")
async def cmd_foo(ctx: tanjun.abc.Context) -> None:
    embed = hikari.Embed(
        title="Beep Boop!",
        description="Thank you for inviting me! Type `/` to see what I can do!",
        color=0x3E77EE,
    )
    await ctx.respond(embed=embed)


@tanjun.as_loader
def load(client: tanjun.abc.Client) -> None:
    client.add_component(listener.copy())
