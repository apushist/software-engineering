using static project.Program;

namespace TestProject1
{
	public class Tests
	{ 
		[Test]
		public void Test1()
		{
			Assert.AreEqual(9, plus(4, 5));
		}

		[Test]
		public void Test2()
		{
			Assert.AreEqual(3, plus(1, 2));
		}

		[Test]
		public void Test3()
		{
			Assert.AreEqual(5, plus(0, 5));
		}
	}
}