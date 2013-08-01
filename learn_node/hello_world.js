console.log("Hello World");

function execute(func, param)
{
  func(param);
}

execute(function say(param) { console.log(param); }, "Hi world");