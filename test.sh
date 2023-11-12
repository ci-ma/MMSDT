for file in ./test/*.txt; do
    # Run the security test plan script for each file
    python3 security_test_plan.py "$file" Threat_AttackPattern_Catalogue.xlsx AttackPattern_Attack_Catalogue.xlsx 
done