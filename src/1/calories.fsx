open System.IO

let text: string = File.ReadAllText("in.txt")
let elves: int list = [for elf: string in text.Trim().Split("\n\n") -> elf.Split("\n") |> Seq.sumBy int]

List.max elves |> printfn "%A" // answer 1
List.sortDescending elves |> Seq.take 3 |> Seq.sumBy int |> printfn "%A" // answer 2