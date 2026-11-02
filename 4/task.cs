using System;
using System.Diagnostics;

namespace DataStructures
{
    public interface IArray<T>
    {
        int Length { get; }
        int ReallocCount { get; }
        string Name { get; }
        void Put(T value);
        void Add(T value, int index);
        T Remove(int index);
        T this[int index] { get; set; }
    }
    public class Array<T> : IArray<T>
    {
        protected int Count { get; set; }
        protected T[] Values { get; set; }
        public int realloc { get; set; } = 0;
        public string Name { get; set; } = "Фиксированный массив";

        public Array(int count = 1)
        {
            if (count < 0)
                throw new ArgumentOutOfRangeException(nameof(count));
            Count = 0;
            Values = new T[count];
        }

        public int Length => Count;
        public int ReallocCount => realloc;

        virtual public void Put(T value)
        {
            if (Count >= Values.Length)
                throw new InvalidOperationException(
                    $"Массив заполнен (Count={Count}, Capacity={Values.Length})");
            Values[Count] = value;
            Count++;
        }

        virtual public void Add(T value, int index)
        {
            if (Count >= Values.Length)
                throw new InvalidOperationException(
                    $"Массив заполнен (Count={Count}, Capacity={Values.Length})");

            Array.Copy(Values, index, Values, index + 1, Count - index);
            Values[index] = value;
            Count++;
        }

        public virtual T Remove(int index)
        {
            T result = Values[index];

            for (int i = index; i < Count - 1; i++)
                Values[i] = Values[i + 1];

            Values[Count - 1] = default;
            Count--;

            return result;
        }

        virtual public T this[int index]
        {
            get
            {
                if (index < 0 || index >= Count)
                    throw new IndexOutOfRangeException(
                        $"index={index}, length={Count}");
                return Values[index];
            }
            set
            {
                if (index < 0 || index >= Count)
                    throw new IndexOutOfRangeException(
                        $"index={index}, length={Count}");
                Values[index] = value;
            }
        }
    }

    internal class VectorArray<T> : Array<T>
    {
        public VectorArray(int count = 1) : base(count)
        {
            Name = "Динамический массив + 1";
        }

        public override void Put(T value)
        {
            if (Count < Values.Length)
            {
                Values[Count] = value;
                Count++;
            }
            else
            {
                realloc++;
                T[] array = new T[Count + 1];
                Array.Copy(Values, array, Count);
                array[Count] = value;
                Count++;
                Values = array;
            }
        }

        public override void Add(T value, int index)
        {
            if (Count < Values.Length)
            {
                Array.Copy(Values, index, Values, index + 1, Count - index);
                Values[index] = value;
                Count++;
            }
            else
            {
                realloc++;
                T[] array = new T[Count + 1];
                Array.Copy(Values, 0, array, 0, index);
                array[index] = value;
                Array.Copy(Values, index, array, index + 1, Count - index);
                Count++;
                Values = array;
            }
        }
    }

    internal class RangeArray<T> : Array<T>
    {
        public RangeArray(int count = 1) : base(count) { Name = "Динамический массив + 100"; }

        public override void Put(T value)
        {
            if (Count < Values.Length)
            {
                Values[Count] = value;
                Count++;
            }
            else
            {
                realloc++;
                T[] array = new T[Count + 100];
                Array.Copy(Values, array, Count);
                array[Count] = value;
                Count++;
                Values = array;
            }
        }

        public override void Add(T value, int index)
        {
            if (Count < Values.Length)
            {
                Array.Copy(Values, index, Values, index + 1, Count - index);
                Values[index] = value;
                Count++;
            }
            else
            {
                realloc++;
                T[] array = new T[Count + 100];
                Array.Copy(Values, 0, array, 0, index);
                array[index] = value;
                Array.Copy(Values, index, array, index + 1, Count - index);
                Count++;
                Values = array;
            }
        }
    }

    internal class FactorArray<T> : Array<T>
    {
        public FactorArray(int count = 1) : base(count) { Name = "Динамический массив * 2"; }

        public override void Put(T value)
        {
            if (Count < Values.Length)
            {
                Values[Count] = value;
                Count++;
            }
            else
            {
                realloc++;
                T[] array = new T[Count * 2];
                Array.Copy(Values, array, Count);
                array[Count] = value;
                Count++;
                Values = array;
            }
        }

        public override void Add(T value, int index)
        {
            if (Count < Values.Length)
            {
                Array.Copy(Values, index, Values, index + 1, Count - index);
                Values[index] = value;
                Count++;
            }
            else
            {
                realloc++;
                T[] array = new T[Count * 2];
                Array.Copy(Values, 0, array, 0, index);
                array[index] = value;
                Array.Copy(Values, index, array, index + 1, Count - index);
                Count++;
                Values = array;
            }
        }
    }

    internal class MatrixArray<T> : IArray<T>
    {
        const int size = 10;
        public int Count { get; protected set; }
        protected T[][] Values { get; set; }
        public int realloc { get; set; } = 0;
        public string Name { get; set; } = "Свободный массив";
        public int Length => Count;
        public int ReallocCount => realloc;

        public MatrixArray()
        {
            Count = 0;
            Values = new T[1][];
            Values[0] = new T[size];
        }
        public T this[int index]
        {
            get { return Values[index / size][index % size]; }
            set { Values[index / size][index % size] = value; }
        }

        public void Put(T value)
        {
            int row = Count / size;
            int col = Count % size;
            if (row < Values.Length)
            {
                Values[row][col] = value;
                Count++;
            }
            else
            {
                realloc++;
                T[][] array = new T[row + 1][];
                Array.Copy(Values, array, row);
                Values = array;
                Values[row] = new T[size];
                Values[row][col] = value;
                Count++;
            }
        }

        public void Add(T value, int index)
        {
            int needRows = (Count + 1 + size - 1) / size;
            if (needRows > Values.Length)
            {
                realloc++;
                T[][] array = new T[Values.Length + 1][];
                Array.Copy(Values, array, Values.Length);
                array[Values.Length] = new T[size];
                Values = array;
            }

            for (int i = Count; i > index; i--)
            {
                Values[i / size][i % size] = Values[(i - 1) / size][(i - 1) % size];
            }

            Values[index / size][index % size] = value;
            Count++;
        }

        public T Remove(int index)
        {
            T result = Values[index / size][index % size];

            for (int i = index; i < Count - 1; i++)
            {
                Values[i / size][i % size] = Values[(i + 1) / size][(i + 1) % size];
            }

            Values[(Count - 1) / size][(Count - 1) % size] = default;

            Count--;
            return result;
        }
    }

    internal class Node<T>(T field)
    {
        readonly T field = field;
        Node<T> link;
        public T Field { get { return field; } set { field = value; } }

        public Node<T> Link
        {
            get { return link; }
            set { link = value; }
        }
    }

    internal class UserList<T>
    {
        Node<T> head;
        public int Count { get; private set; }

        public UserList()
        {
            head = null;
            Count = 0;
        }
        public void Insert(T val, int index = 0)
        {
            Node<T> node = new Node<T>(val);

            if (index == 0)
            {
                node.Link = head;
                head = node;
            }
            else
            {
                Node<T> curr = head;
                Node<T> prev = null;
                for (int i = 0; i < index; i++)
                {
                    prev = curr;
                    curr = curr.Link;
                }
                prev.Link = node;
                node.Link = curr;
            }
            Count++;
        }

        public T Remove(int index)
        {
            T result;
            if (index == 0)
            {
                result = head!.Field;
                head = head.Link;
            }
            else
            {
                Node<T> curr = head;
                Node<T> prev = null;
                for (int i = 0; i < index; i++)
                {
                    prev = curr;
                    curr = curr.Link;
                }
                result = curr.Field;
                prev.Link = curr.Link;
            }
            Count--;
            return result;
        }

        public T this[int index]
        {
            get
            {
                if (index >= Count) return default;
                Node<T> curr = head;
                for (int i = 0; i < index; i++)
                    curr = curr.Link;
                return curr.Field;
            }
            set
            {
                if (index >= Count) return;
                Node<T> curr = head;
                for (int i = 0; i < index; i++)
                    curr = curr.Link;
                curr.Field = value;
            }
        }
    }

    internal class UserListWrapper<T> : IArray<T>
    {
        private readonly UserList<T> list = new();

        public int Length => list.Count;
        public int ReallocCount => 0;
        public string Name => "Связный список";

        public void Put(T value) => list.Insert(value, list.Count);
        public void Add(T value, int index) => list.Insert(value, index);
        public T Remove(int index) => list.Remove(index);

        public T this[int index]
        {
            get => list[index];
            set => list[index] = value;
        }
    }

    internal class Program
    {
        static void Main()
        {
            int[] sizes = { 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000 };

            int opsForAddRemove = 1000;

            for (int s = 0; s < sizes.Length; s++)
            {
                int N = sizes[s];

                int[] values = new int[N];
                Random rnd = new Random(1);
                for (int i = 0; i < N; i++)
                    values[i] = rnd.Next(0, N);

                Console.WriteLine();
                Console.WriteLine($"=== N = {N}, OPS = {opsForAddRemove} ===");
                Console.WriteLine();

                Benchmark(new FactorArray<int>(), new FactorArray<int>(), new FactorArray<int>(), values, opsForAddRemove);
                Benchmark(new RangeArray<int>(), new RangeArray<int>(), new RangeArray<int>(), values, opsForAddRemove);
                Benchmark(new VectorArray<int>(), new VectorArray<int>(), new VectorArray<int>(), values, opsForAddRemove);
                Benchmark(new MatrixArray<int>(), new MatrixArray<int>(), new MatrixArray<int>(), values, opsForAddRemove);
                Benchmark(new UserListWrapper<int>(), new UserListWrapper<int>(), new UserListWrapper<int>(), values, opsForAddRemove);
            }
        }

        static void Benchmark(IArray<int> forPut,
                         IArray<int> forAdd,
                         IArray<int> forRemove,
                         int[] values,
                         int ops)
        {
            Console.WriteLine(forPut.Name);
            Stopwatch sw = new Stopwatch();
            bool timeout = false;

            sw.Restart();
            for (int i = 0; i < values.Length; i++)
            {
                forPut.Put(values[i]);
                if ((i & 1023) == 0 && sw.Elapsed.TotalSeconds >= 120.0) { timeout = true; break; }
            }
            sw.Stop();
            Console.WriteLine("Put".PadRight(10) + (timeout ? "> 120.000" : sw.Elapsed.TotalMilliseconds.ToString("F3")).PadLeft(10));

            sw.Restart();
            timeout = false;
            for (int i = 0; i < values.Length; i++)
            {
                forAdd.Put(values[i]);
                if ((i & 1023) == 0 && sw.Elapsed.TotalSeconds >= 120.0) { timeout = true; break; }
            }

            if (timeout)
            {
                Console.WriteLine("Add".PadRight(10) + "> 120.000".PadLeft(10));
            }
            else
            {
                sw.Restart();
                for (int i = 0; i < ops; i++)
                {
                    forAdd.Add(values[i % values.Length], forAdd.Length / 2);
                    if ((i & 1023) == 0 && sw.Elapsed.TotalSeconds >= 120.0) { timeout = true; break; }
                }
                sw.Stop();
                Console.WriteLine("Add".PadRight(10) + (timeout ? "> 120.000" : sw.Elapsed.TotalMilliseconds.ToString("F3")).PadLeft(10));
            }


            sw.Restart();
            timeout = false;
            for (int i = 0; i < values.Length; i++)
            {
                forRemove.Put(values[i]);
                if ((i & 1023) == 0 && sw.Elapsed.TotalSeconds >= 120.0) { timeout = true; break; }
            }

            if (timeout)
            {
                Console.WriteLine("Remove".PadRight(10) + "> 120.000".PadLeft(10));
            }
            else
            {
                sw.Restart();
                for (int i = 0; i < ops; i++)
                {
                    if (forRemove.Length == 0) break;
                    forRemove.Remove(forRemove.Length / 2);
                    if ((i & 1023) == 0 && sw.Elapsed.TotalSeconds >= 120.0) { timeout = true; break; }
                }
                sw.Stop();
                Console.WriteLine("Remove".PadRight(10) + (timeout ? "> 120.000" : sw.Elapsed.TotalMilliseconds.ToString("F3")).PadLeft(10));
            }

            Console.WriteLine();
        }
    }
}
