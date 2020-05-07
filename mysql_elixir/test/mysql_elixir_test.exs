defmodule MysqlElixirTest do
  use ExUnit.Case
  doctest MysqlElixir

  test "greets the world" do
    assert MysqlElixir.hello() == :world
  end
end
